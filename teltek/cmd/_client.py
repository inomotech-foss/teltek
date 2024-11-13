import logging
from collections.abc import Iterable
from typing import Any

import teltek.parameters
from teltek.cmd._batcher import iter_param_batches
from teltek.cmd._device_id import DeviceId
from teltek.cmd.transport import Transport

_LOGGER = logging.getLogger(__name__)


class CommandClient:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    async def get_full_parameters(self, device_id: DeviceId) -> dict[str, Any]:
        param_ids = list(teltek.parameters.db.iter_parameter_ids())
        raw_params = await self.get_raw_parameters(device_id, param_ids)
        return teltek.parameters.map_raw_parameters(raw_params)

    async def get_raw_parameters(
        self, device_id: DeviceId, param_ids: Iterable[int]
    ) -> dict[int, str]:
        batches = list(iter_param_batches(param_ids, self._transport.max_command_len))
        param_count = sum(len(batch) for batch in batches)
        _LOGGER.info(
            "requesting %s parameter(s) in %d batches", param_count, len(batches)
        )

        params: dict[int, str] = {}
        for i, batch in enumerate(batches):
            _LOGGER.debug("getting batch %d/%s", i + 1, len(batches))
            batch_params = await self._get_raw_parameters_batch(device_id, *batch)
            params.update(batch_params)
        return params

    async def _get_raw_parameters_batch(
        self, device_id: DeviceId, *param_ids: int
    ) -> dict[int, str]:
        response = await self.run_command(
            device_id, "getparam " + ";".join(map(str, param_ids))
        )
        params: dict[int, str] = {}
        raw_params = response.split(";")

        # first param is special: Param ID:1000 Value:300
        first_param = raw_params[0]
        param_id = first_param[9:]
        param_id, _, param_value = param_id.partition(" ")
        param_value = param_value[6:]
        params[int(param_id)] = param_value

        # others are: 10000:60
        for rest_param in raw_params[1:]:
            param_id, _, param_value = rest_param.partition(":")
            params[int(param_id)] = param_value

        return params

    async def run_command(
        self, device_id: DeviceId, command: str, *, retry: int = 2
    ) -> str:
        assert retry >= 0
        last_exc: Exception | None = None
        for _ in range(retry + 1):
            if last_exc:
                _LOGGER.warning("retrying command")
            try:
                return await self._transport.run_command(device_id, command)
            except Exception as exc:
                last_exc = exc
        assert last_exc is not None
        raise last_exc
