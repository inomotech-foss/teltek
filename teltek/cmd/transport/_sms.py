import asyncio
import dataclasses
import logging
from datetime import UTC, datetime
from types import TracebackType
from typing import Any, Literal, Self

import bs4
import httpx

from teltek.cmd._device_id import DeviceId
from teltek.cmd.transport._abc import Transport

_LOGGER = logging.getLogger(__name__)


class TruphoneTransport(Transport):
    _ACCOUNT_BASE_URL = "https://account.truphone.com"
    _IOT_BASE_URL = "https://iot.truphone.com"
    _POLL_INTERVAL = 1
    _RESP_TIMEOUT = 20

    def __init__(
        self,
        *,
        email: str,
        password: str,
        device_username: str = "",
        device_password: str = "",
    ) -> None:
        super().__init__()
        self._email = email
        self._password = password
        self._device_username = device_username
        self._device_password = device_password
        self._max_command_len = 160 - len(
            f"{self._device_username} {self._device_password} "
        )
        self._client = httpx.AsyncClient()
        self._reader_task: asyncio.Task[None] | None = None
        self._active_event = asyncio.Event()
        self._pending_requests: dict[str, tuple[asyncio.Future[str], datetime]] = {}
        self._seen_responses: set[int] = set()

    async def __aenter__(self) -> Self:
        assert self._reader_task is None
        self._client = await self._client.__aenter__()
        await self._login()
        self._reader_task = asyncio.create_task(self.__reader())
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        if self._reader_task is not None:
            self._reader_task.cancel()
            self._reader_task = None
        await self._client.__aexit__(exc_type, exc_value, traceback)
        self._active_event.clear()
        self._pending_requests.clear()
        self._seen_responses.clear()

    @property
    def max_command_len(self) -> int:
        return self._max_command_len

    async def run_command(self, device_id: DeviceId, command: str) -> str:
        assert device_id.iccid is not None, "ICCID required"
        return await self._run_command_iccid(device_id.iccid, command)

    async def _run_command_iccid(self, iccid: str, command: str) -> str:
        assert iccid not in self._pending_requests
        message = f"{self._device_username} {self._device_password} {command}"
        (fut, _) = self._pending_requests[iccid] = (
            asyncio.Future(),
            datetime.now(tz=UTC),
        )
        self._active_event.set()
        try:
            await self._post_sms(iccid, message)
            return await asyncio.wait_for(fut, timeout=self._RESP_TIMEOUT)
        finally:
            self._pending_requests.pop(iccid)

    async def _get_csrf_token(self, html: str) -> str:
        doc = bs4.BeautifulSoup(html, "lxml")
        input_el = doc.select_one('input[name="csrfmiddlewaretoken"]')
        if input_el is None:
            raise ValueError("No CSRF token found")
        csrf_token = input_el["value"]
        assert isinstance(csrf_token, str)
        return csrf_token

    async def _login(self) -> None:
        url = f"{self._ACCOUNT_BASE_URL}/login"
        resp = await self._client.get(url)
        csrf_token = await self._get_csrf_token(resp.text)
        _LOGGER.debug("Logging in with CSRF token %s", csrf_token)
        resp = await self._client.post(
            url,
            data={
                "email": self._email,
                "password": self._password,
                "csrfmiddlewaretoken": csrf_token,
            },
        )
        if resp.status_code == 302:
            _LOGGER.info("Successfully logged in")
            return
        resp.raise_for_status()

    async def _get_sms_response(
        self, *, start: int = 0, length: int = 50
    ) -> "_SmsResponse":
        resp = await self._client.get(
            f"{self._IOT_BASE_URL}/browsers/sms-response",
            params={
                "start": start,
                "length": length,
                "columns[0][data]": "date",
                "columns[0][name]": "date",
                "order[0][column]": "0",
                "order[0][dir]": "desc",
            },
        )
        resp.raise_for_status()
        return _SmsResponse.from_dict(resp.json())

    async def _post_sms(
        self,
        iccid: str,
        message: str,
        source_msisdn: str = "6260",
    ) -> None:
        url = f"{self._IOT_BASE_URL}/sms/"
        resp = await self._client.get(url)
        csrf_token = await self._get_csrf_token(resp.text)
        _LOGGER.debug("Sending SMS with CSRF token %s", csrf_token)
        resp = await self._client.post(
            url,
            data={
                "csrfmiddlewaretoken": csrf_token,
                "source_msisdn": source_msisdn,
                "normal_sims": iccid,
                "message": message,
                "normal_sms": "True",
                "send_normal_sms_submit": "Send",
            },
            headers={"Referer": url},
        )
        if resp.status_code == 302:
            _LOGGER.info("SMS sent")
            return
        resp.raise_for_status()

    async def __poll_once(self) -> None:
        response = await self._get_sms_response()
        for sms_resp in response.data:
            sms_resp_hash = hash(sms_resp)
            if sms_resp_hash in self._seen_responses:
                continue
            self._seen_responses.add(sms_resp_hash)
            if sms_resp.sms_type != "Mobile Originated":
                continue
            pair = self._pending_requests.get(sms_resp.sim_card_iccid)
            if pair is None:
                continue
            (fut, start_time) = pair
            if fut.done():
                continue
            # round start_time to the nearest minute
            start_time = start_time.replace(second=0, microsecond=0)
            if sms_resp.date_datetime < start_time:
                # sms received before the command was sent
                continue
            fut.set_result(sms_resp.content)

    async def __reader(self) -> None:
        while True:
            await self._active_event.wait()

            first = True
            while self._pending_requests:
                if first:
                    first = False
                else:
                    await asyncio.sleep(self._POLL_INTERVAL)
                try:
                    await self.__poll_once()
                except Exception:
                    _LOGGER.exception("failed to poll")

            self._active_event.clear()


@dataclasses.dataclass(kw_only=True, frozen=True)
class _Sms:
    origin: str
    content: str
    sim_card: str
    destination: str
    organization_name: str
    status: str
    date: str
    delivery_status: str
    sms_type: Literal["Mobile Originated"] | Literal["Mobile Terminated"]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(**data)

    @property
    def sim_card_iccid(self) -> str:
        # sim_card	'<a href="/sims/8944477100002778325/">8944477100002778325</a>'
        sim_card_el = bs4.BeautifulSoup(self.sim_card, "lxml")
        return sim_card_el.a.string  # type: ignore

    @property
    def date_datetime(self) -> datetime:
        # 2024/11/12 23:01 UTC
        dt = datetime.strptime(self.date, "%Y/%m/%d %H:%M %Z")
        if dt.tzinfo is None:
            return dt.replace(tzinfo=UTC)
        return dt


@dataclasses.dataclass(kw_only=True, frozen=True)
class _SmsResponse:
    records_total: int
    records_filtered: int
    data: list[_Sms]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            records_total=data["recordsTotal"],
            records_filtered=data["recordsFiltered"],
            data=[_Sms(**record) for record in data["data"]],
        )
