import dataclasses
import re
from datetime import datetime
from typing import Self


@dataclasses.dataclass(frozen=True)
class AccelVector:
    x: float
    y: float
    z: float


# Calibrated! Last [2024-11-16 16:26:22] Qual:0.82 GROUND -> X:0.277259 Y:0.167735 Z:0.946040 SIDE -> X:-0.290085 Y:-0.924078 Z:0.248857 Pos:0
# Not Calibrated! Last [1970-01-01 00:00:00] Qual:0.00 GROUND -> X:0.000000 Y:0.000000 Z:0.000000 SIDE -> X:0.000000 Y:0.000000 Z:0.000000 Pos:0
_RE_CALIBRATION = re.compile(
    r"(Not )?Calibrated! Last \[(.+?)\] Qual:(.+?) GROUND -> X:(.+?) Y:(.+?) Z:(.+?) SIDE -> X:(.+?) Y:(.+?) Z:(.+?) Pos:(.+?)"
)


@dataclasses.dataclass(frozen=True)
class AccelCalibrationInfo:
    calibrated: bool
    last: datetime
    quality: float
    ground: AccelVector
    side: AccelVector
    pos: int

    @classmethod
    def parse(cls, s: str) -> Self:
        m = _RE_CALIBRATION.match(s)
        if m is None:
            raise ValueError(f"Failed to parse calibration info: {s}")
        calibrated = m.group(1) is None
        ground = AccelVector(*map(float, m.group(4, 5, 6)))
        side = AccelVector(*map(float, m.group(7, 8, 9)))
        return cls(
            calibrated=calibrated,
            last=datetime.fromisoformat(m.group(2)),
            quality=float(m.group(3)),
            ground=ground,
            side=side,
            pos=int(m.group(10)),
        )
