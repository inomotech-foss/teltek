import asyncio
import logging
from types import TracebackType
from typing import Self, cast

import parse  # type: ignore
from aiomqtt import Client

from teltek.cmd._device_id import DeviceId
from teltek.cmd.transport._abc import Transport
from teltek.codec import Codec12, Codec12Type, CodecId, MessageFrame

_LOGGER = logging.getLogger(__name__)


class MqttTransport(Transport):
    def __init__(
        self,
        client: Client,
        *,
        command_topic: str = "{imei}/commands",
        data_topic: str = "{imei}/data",
    ) -> None:
        super().__init__()
        self._client = client
        self._command_topic = command_topic
        self._data_topic = parse.compile(data_topic)  # type: ignore
        self._reader_task: asyncio.Task[None] | None = None
        self._pending_requests: dict[str, asyncio.Future[Codec12]] = {}
        self._subscribed_imeis: set[str] = set()

    async def __aenter__(self) -> Self:
        assert self._reader_task is None
        self._client = await self._client.__aenter__()
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
        self._pending_requests.clear()
        self._subscribed_imeis.clear()

    async def run_command(self, device_id: DeviceId, command: str) -> str:
        assert device_id.imei is not None, "IMEI required"
        return await self._run_command_imei(device_id.imei, command)

    async def _run_command_imei(self, imei: str, command: str) -> str:
        assert imei not in self._pending_requests

        command_topic = self._get_command_topic(imei)
        data_topic = self._get_data_topic(imei)

        if imei not in self._subscribed_imeis:
            self._subscribed_imeis.add(imei)
            await self._client.subscribe(data_topic)

        req_frame = Codec12(type=Codec12Type.REQUEST, content=command).to_frame()
        fut = self._pending_requests[imei] = asyncio.Future()
        try:
            await self._client.publish(command_topic, req_frame.encode())
            response = await asyncio.wait_for(fut, timeout=20)
            return response.content
        finally:
            self._pending_requests.pop(imei)

    @property
    def max_command_len(self) -> int:
        return 500

    def _get_command_topic(self, imei: str) -> str:
        return self._command_topic.format(imei=imei)

    def _get_data_topic(self, imei: str) -> str:
        format_str = cast(str, self._data_topic.format)  # type: ignore
        return format_str.format(imei=imei)

    async def __reader(self) -> None:
        async for msg in self._client.messages:
            res = self._data_topic.parse(msg.topic.value, evaluate_result=True)  # type: ignore
            if res is None:
                continue
            # evaluate_result is True, so we get a Result
            assert isinstance(res, parse.Result)
            imei = cast(str, res["imei"])

            fut = self._pending_requests.get(imei)
            if fut is None or fut.done():
                continue
            try:
                frame = MessageFrame.decode(msg.payload)  # type: ignore
            except Exception as exc:
                _LOGGER.exception("failed to decode message", exc_info=exc)
                continue
            try:
                if frame.codec_id == CodecId.CODEC_12:
                    codec = Codec12.from_frame(frame)
                    fut.set_result(codec)
            except Exception as exc:
                fut.set_exception(exc)
