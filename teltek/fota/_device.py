import dataclasses
from typing import Any, Self


@dataclasses.dataclass(frozen=True)
class Device:
    imei: int
    description: str
    iccid: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            imei=int(data["imei"]),
            description=str(data["description"]),
            iccid=str(data["iccid"]),
        )
