import asyncio
import logging
from collections.abc import Iterable
from typing import Any

import teltek.parameters
from teltek.cmd._accelerometer import AccelCalibrationInfo
from teltek.cmd._batcher import iter_param_batches, iter_set_param_batches
from teltek.cmd._device_id import DeviceId
from teltek.cmd.transport import Transport

_LOGGER = logging.getLogger(__name__)


class CommandClient:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    async def get_accelerometer_auto_calibration(
        self, device_id: DeviceId
    ) -> AccelCalibrationInfo:
        resp = await self.run_command(device_id, "auto_calibrate:get")
        return AccelCalibrationInfo.parse(resp)

    async def get_full_parameters(self, device_id: DeviceId) -> dict[str, Any]:
        param_ids = list(teltek.parameters.db.iter_parameter_ids())
        raw_params = await self.get_raw_parameters(device_id, param_ids)
        return teltek.parameters.map_raw_parameters(raw_params)

    async def set_full_parameters(
        self,
        device_id: DeviceId,
        values: dict[str, Any],
        *,
        old_values: dict[str, Any] | None = None,
    ) -> None:
        raw_values = teltek.parameters.map_parameters_to_raw(values)
        if old_values:
            old_raw_values = teltek.parameters.map_parameters_to_raw(old_values)
            # Only set parameters that have changed
            raw_values = {
                id: raw
                for id, raw in raw_values.items()
                if old_raw_values.get(id) != raw
            }
        await self.set_raw_parameters(device_id, raw_values)

    async def get_raw_parameters(
        self,
        device_id: DeviceId,
        param_ids: Iterable[int],
        *,
        attempts_per_batch: int = 3,
    ) -> dict[int, str]:
        batches = list(iter_param_batches(param_ids, self._transport.max_command_len))
        param_count = sum(len(batch) for batch in batches)
        _LOGGER.info(
            "%s: requesting %s parameter(s) in %d batches",
            device_id,
            param_count,
            len(batches),
        )

        params: dict[int, str] = {}
        for batch_nr, batch in enumerate(batches, 1):
            _LOGGER.debug("%s: getting batch %d/%d", device_id, batch_nr, len(batches))
            last_exc = None
            for attempt in range(1, attempts_per_batch + 1):
                if last_exc:
                    _LOGGER.warning(
                        "%s: retrying batch %d (attempt %d/%d)",
                        device_id,
                        batch_nr,
                        attempt,
                        attempts_per_batch,
                    )
                try:
                    batch_params = await self._get_raw_parameters_batch(
                        device_id, *batch
                    )
                except asyncio.TimeoutError:
                    raise
                except Exception as exc:
                    last_exc = exc
                else:
                    last_exc = None
                    params.update(batch_params)
                    break
            if last_exc:
                raise last_exc

        return params

    async def set_raw_parameters(
        self,
        device_id: DeviceId,
        params: dict[int, str],
        *,
        attempts_per_batch: int = 3,
    ) -> None:
        batches = list(
            iter_set_param_batches(params.items(), self._transport.max_command_len)
        )
        param_count = sum(len(batch) for batch in batches)
        _LOGGER.info(
            "%s: setting %s parameter(s) in %d batches",
            device_id,
            param_count,
            len(batches),
        )

        for batch_nr, batch in enumerate(batches, 1):
            _LOGGER.debug("%s: setting batch %d/%d", device_id, batch_nr, len(batches))
            last_exc = None
            for attempt in range(1, attempts_per_batch + 1):
                if last_exc:
                    _LOGGER.warning(
                        "%s: retrying batch %d (attempt %d/%d)",
                        device_id,
                        batch_nr,
                        attempt,
                        attempts_per_batch,
                    )

                try:
                    await self._set_raw_parameters_batch(device_id, batch)
                except asyncio.TimeoutError:
                    raise
                except Exception as exc:
                    last_exc = exc
                else:
                    last_exc = None
                    break
            if last_exc:
                raise last_exc

    async def _get_raw_parameters_batch(
        self,
        device_id: DeviceId,
        *param_ids: int,
    ) -> dict[int, str]:
        response = await self.run_command(
            device_id, "getparam " + ";".join(map(str, param_ids))
        )
        params: dict[int, str] = {}
        raw_params = response.split(";")

        # first param is special: Param ID:1000 Value:300
        first_param = raw_params[0]
        first_param = first_param[9:]
        try:
            param_id, _, param_value = first_param.partition(" ")
            param_value = param_value[6:]
            param_id = int(param_id)
        except ValueError as exc:
            raise ValueError(f"Failed to parse first param {first_param!r}") from exc
        params[param_id] = param_value

        # others are: 10000:60
        for rest_param in raw_params[1:]:
            try:
                param_id, _, param_value = rest_param.partition(":")
                param_id = int(param_id)
            except ValueError as exc:
                raise ValueError(f"Failed to parse param {rest_param!r}") from exc
            params[param_id] = param_value

        _ensure_param_ids_match(param_ids, params.keys())

        return params

    async def _set_raw_parameters_batch(
        self,
        device_id: DeviceId,
        params: dict[int, str],
    ) -> None:
        await self.run_command(
            device_id,
            "setparam " + ";".join(f"{id}:{raw}" for id, raw in params.items()),
        )

    async def run_command(
        self,
        device_id: DeviceId,
        command: str,
        *,
        attempts: int = 3,
    ) -> str:
        assert attempts >= 1
        last_exc: Exception | None = None
        for attempt in range(1, attempts + 1):
            if last_exc:
                _LOGGER.warning(
                    "%s: retrying command (attempt %s/%s)",
                    device_id,
                    attempt,
                    attempts,
                )
            try:
                return await self._transport.run_command(device_id, command)
            except Exception as exc:
                last_exc = exc
        assert last_exc is not None
        raise last_exc


def _ensure_param_ids_match(requested: Iterable[int], received: Iterable[int]) -> bool:
    requested_set = set(requested)
    received_set = set(received)
    if requested_set.isdisjoint(received_set):
        raise ValueError("Parameter response doesn't match request")
    if extra := received_set - requested_set:
        _LOGGER.warning(
            "Received additional parameters that weren't requested %s", extra
        )
    if missing := requested_set - received_set:
        _LOGGER.warning("Requested parameters that weren't received %s", missing)
        _LOGGER.debug("Requested: %s", requested)
    return not (extra or missing)
