from datetime import datetime

from teltek.cmd import AccelCalibrationInfo, AccelVector


def test_calibrated():
    info = AccelCalibrationInfo.parse(
        "Calibrated! Last [2024-11-16 16:26:22] Qual:0.82 GROUND -> X:0.277259 Y:0.167735 Z:0.946040 SIDE -> X:-0.290085 Y:-0.924078 Z:0.248857 Pos:0"
    )
    assert info == AccelCalibrationInfo(
        calibrated=True,
        last=datetime.fromisoformat("2024-11-16T16:26:22"),
        quality=0.82,
        ground=AccelVector(x=0.277259, y=0.167735, z=0.946040),
        side=AccelVector(x=-0.290085, y=-0.924078, z=0.248857),
        pos=0,
    )


def test_not_calibrated():
    info = AccelCalibrationInfo.parse(
        "Not Calibrated! Last [1970-01-01 00:00:00] Qual:0.00 GROUND -> X:0.000000 Y:0.000000 Z:0.000000 SIDE -> X:0.000000 Y:0.000000 Z:0.000000 Pos:0"
    )
    assert info == AccelCalibrationInfo(
        calibrated=False,
        last=datetime.fromisoformat("1970-01-01T00:00:00"),
        quality=0.00,
        ground=AccelVector(x=0.000000, y=0.000000, z=0.000000),
        side=AccelVector(x=0.000000, y=0.000000, z=0.000000),
        pos=0,
    )
