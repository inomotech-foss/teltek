import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True)
class DeviceId:
    imei: str | None = None
    iccid: str | None = None

    def __str__(self) -> str:
        if self.imei is not None:
            return self.imei
        if self.iccid is not None:
            return self.iccid
        return "unknown"
