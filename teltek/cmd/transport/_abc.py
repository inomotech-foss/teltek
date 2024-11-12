import abc

from teltek.cmd._device_id import DeviceId


class Transport(abc.ABC):
    @property
    @abc.abstractmethod
    def max_command_len(self) -> int: ...

    @abc.abstractmethod
    async def run_command(self, device_id: DeviceId, command: str) -> str: ...
