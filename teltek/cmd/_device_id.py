import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True)
class DeviceId:
    imei: str | None = None
    iccid: str | None = None
