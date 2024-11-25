from collections.abc import AsyncIterable
from types import TracebackType
from typing import Literal, Self

import httpx

from teltek.fota._device import Device
from teltek.fota._file import FileType
from teltek.fota._pagination import PaginatedData


class FotaApi:
    def __init__(self, token: str) -> None:
        self._client = httpx.AsyncClient(
            base_url="https://api.teltonika.lt",
            headers={"Authorization": f"Bearer {token}"},
        )

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        return await self._client.__aexit__(exc_type, exc_value, traceback)

    async def _upload_file(
        self,
        *,
        type: FileType,
        description: str | None = None,
    ) -> None:
        # TODO
        data = {
            key: value
            for key, value in (
                ("company_ids", ["TODO"]),
                ("type", type.value),
                ("description", description),
            )
            if value is not None
        }
        resp = await self._client.post(
            "/files",
            data=data,
            files={"file": "TODO"},
        )
        resp.raise_for_status()

    async def iter_devices(self) -> AsyncIterable[Device]:
        page_data = await self.devices_page(page=1)
        while True:
            for device in page_data.data:
                yield device
            if page_data.current_page >= page_data.last_page:
                break
            page_data = await self.devices_page(page=page_data.current_page + 1)

    async def devices_page(
        self,
        *,
        imei: list[int] | None = None,
        company_id: list[int] | None = None,
        group_id: list[int] | None = None,
        model: list[str] | None = None,
        current_firmware: list[str] | None = None,
        current_configuration: list[str] | None = None,
        activity_status: list[int] | None = None,
        task_queue: list[int] | None = None,
        query: str | None = None,
        page: int = 1,
        per_page: int = 25,
        sort: Literal["imei", "description", "model", "serial", "created_at"]
        | None = None,
        order: Literal["asc", "desc"] | None = None,
    ) -> PaginatedData[Device]:
        params = {
            key: value
            for key, value in (
                ("imei", imei),
                ("company_id", company_id),
                ("group_id", group_id),
                ("model", model),
                ("current_firmware", current_firmware),
                ("current_configuration", current_configuration),
                ("activity_status", activity_status),
                ("task_queue", task_queue),
                ("query", query),
                ("page", page),
                ("per_page", per_page),
                ("sort", sort),
                ("order", order),
            )
            if value is not None
        }
        resp = await self._client.get(
            "/devices",
            params=params,
        )
        resp.raise_for_status()
        return PaginatedData.from_dict(Device, resp.json())
