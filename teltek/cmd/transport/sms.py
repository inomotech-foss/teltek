import abc


class SmsApi(abc.ABC):
    @abc.abstractmethod
    async def send(self, iccid: str, message: str) -> None: ...
