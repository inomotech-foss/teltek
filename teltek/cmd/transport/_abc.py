import abc


class Transport(abc.ABC):
    @property
    @abc.abstractmethod
    def max_command_len(self) -> int: ...

    async def run_command(self, imei: str, command: str) -> str: ...
