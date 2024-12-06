from datetime import datetime

from teltek.cmd import AccelCalibrationInfo, AccelVector


def test_calibrated():
    info = AccelCalibrationInfo.parse(
        "Calibrated! Last [2024-11-16 16:26:22] Qual:0.82 GROUND -> X:0.277259 Y:0.167735 Z:0.946040 SIDE -> X:-0.290085 Y:-0.924078 Z:0.248857 Pos:0"
    )
    assert info == AccelCalibrationInfo(
        calibrated=True,
        full=None,
        last=datetime.fromisoformat("2024-11-16T16:26:22"),
        quality=0.82,
        ground=AccelVector(x=0.277259, y=0.167735, z=0.946040),
        side=AccelVector(x=-0.290085, y=-0.924078, z=0.248857),
        pos=0,
        qt1=None,
        qt2=None,
        qt3=None,
    )

    info = AccelCalibrationInfo.parse(
        """IMEI:071 Calibrated! Full? Yes! Last [2024-12-05 20:23:34] In [99:99] Qual:1.00 Pos:0
G{-0.941;-0.337;-0.031}
R{-0.371;0.912;0.161}
QT1:0.75 QT2:0.00 QT3:0"""
    )
    assert info == AccelCalibrationInfo(
        calibrated=True,
        full=True,
        last=datetime.fromisoformat("2024-12-05T20:23:34"),
        quality=1.00,
        ground=AccelVector(x=-0.941, y=-0.337, z=-0.031),
        side=AccelVector(x=-0.371, y=0.912, z=0.161),
        pos=0,
        qt1=0.75,
        qt2=0.00,
        qt3=0,
    )


def test_not_calibrated():
    info = AccelCalibrationInfo.parse(
        "Not Calibrated! Last [1970-01-01 00:00:00] Qual:0.00 GROUND -> X:0.000000 Y:0.000000 Z:0.000000 SIDE -> X:0.000000 Y:0.000000 Z:0.000000 Pos:0"
    )
    assert info == AccelCalibrationInfo(
        calibrated=False,
        full=None,
        last=datetime.fromisoformat("1970-01-01T00:00:00"),
        quality=0.00,
        ground=AccelVector(x=0.000000, y=0.000000, z=0.000000),
        side=AccelVector(x=0.000000, y=0.000000, z=0.000000),
        pos=0,
        qt1=None,
        qt2=None,
        qt3=None,
    )

    info = AccelCalibrationInfo.parse(
        """IMEI:963 Not Calibrated! Full? No! Last [1970-01-01 00:00:00] In [00:00] Qual:0.00 Pos:0
G{0.000;0.000;0.000}
R{0.000;0.000;0.000}
QT1:0.00 QT2:0.00 QT3:0"""
    )
    assert info == AccelCalibrationInfo(
        calibrated=False,
        full=False,
        last=datetime.fromisoformat("1970-01-01T00:00:00"),
        quality=0.00,
        ground=AccelVector(x=0.0, y=0.0, z=0.0),
        side=AccelVector(x=0.0, y=0.0, z=0.0),
        pos=0,
        qt1=0.00,
        qt2=0.00,
        qt3=0,
    )
