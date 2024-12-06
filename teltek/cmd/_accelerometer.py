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
_RE_CALIBRATION1 = re.compile(
    r"""
    (?P<not_calibrated>Not\ )?Calibrated!
    \ Last\ \[(?P<last>.+?)\]
    \ Qual:(?P<qual>.+?)
    \ GROUND\ ->\ X:(?P<g_x>.+?)\ Y:(?P<g_y>.+?)\ Z:(?P<g_z>.+?)
    \ SIDE\ ->\ X:(?P<s_x>.+?)\ Y:(?P<s_y>.+?)\ Z:(?P<s_z>.+?)\ Pos:(?P<pos>.+?)
    """,
    re.VERBOSE,
)
# IMEI:963 Not Calibrated! Full? No! Last [1970-01-01 00:00:00] In [00:00] Qual:0.00 Pos:0\nG{0.000;0.000;0.000}\nR{0.000;0.000;0.000}\nQT1:0.00 QT2:0.00 QT3:0
_RE_CALIBRATION2 = re.compile(
    r"""
    IMEI:\d+
    \ (?P<not_calibrated>Not\ )?Calibrated!
    \ Full\?\ (?P<full_yes_no>Yes|No)!
    \ Last\ \[(?P<last>.+?)\]\ In\ \[(?P<in>.+?)\]
    \ Qual:(?P<qual>.+?)
    \ Pos:(?P<pos>.+?)
    \nG{(?P<g_x>.+?);(?P<g_y>.+?);(?P<g_z>.+?)}
    \nR{(?P<s_x>.+?);(?P<s_y>.+?);(?P<s_z>.+?)}
    \nQT1:(?P<qt1>.+?) QT2:(?P<qt2>.+?) QT3:(?P<qt3>.+?)
    """,
    re.VERBOSE,
)


@dataclasses.dataclass(frozen=True)
class AccelCalibrationInfo:
    calibrated: bool
    full: bool | None
    last: datetime
    quality: float
    ground: AccelVector
    side: AccelVector
    pos: int
    qt1: float | None
    qt2: float | None
    qt3: float | None

    @classmethod
    def parse(cls, s: str) -> Self:
        m = _RE_CALIBRATION1.match(s)
        if m is None:
            m = _RE_CALIBRATION2.match(s)
        if m is None:
            raise ValueError(f"Failed to parse calibration info: {s}")
        calibrated = m.group("not_calibrated") is None
        ground = AccelVector(*map(float, m.group("g_x", "g_y", "g_z")))
        side = AccelVector(*map(float, m.group("s_x", "s_y", "s_z")))

        try:
            full = m.group("full_yes_no") == "Yes"
        except IndexError:
            full = None

        try:
            qt1, qt2, qt3 = map(float, m.group("qt1", "qt2", "qt3"))
        except IndexError:
            qt1 = qt2 = qt3 = None

        return cls(
            calibrated=calibrated,
            full=full,
            last=datetime.fromisoformat(m.group("last")),
            quality=float(m.group("qual")),
            ground=ground,
            side=side,
            pos=int(m.group("pos")),
            qt1=qt1,
            qt2=qt2,
            qt3=qt3,
        )
