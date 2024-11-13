from collections.abc import Iterator

from ._accelerometer import ACCELEROMETER
from ._data_acquisition_mode import DATA_ACQUISITION_MODE
from ._features import FEATURES
from ._gprs import GPRS
from ._gsm import GSM
from ._io import IO
from ._obd import OBD
from ._sms_call import SMS
from ._system import SYSTEM
from ._tracking_on_demand import TRACKING_ON_DEMAND
from ._trip_odometer import TRIP_ODOMETER

__all__ = [
    "ACCELEROMETER",
    "ALL_GROUPS",
    "DATA_ACQUISITION_MODE",
    "FEATURES",
    "GPRS",
    "GSM",
    "IO",
    "OBD",
    "SMS",
    "SYSTEM",
    "TRACKING_ON_DEMAND",
    "TRIP_ODOMETER",
    "iter_parameter_ids",
]

ALL_GROUPS = [
    ACCELEROMETER,
    DATA_ACQUISITION_MODE,
    FEATURES,
    GPRS,
    GSM,
    IO,
    OBD,
    SMS,
    SYSTEM,
    TRACKING_ON_DEMAND,
    TRIP_ODOMETER,
]


def iter_parameter_ids() -> Iterator[int]:
    for group in ALL_GROUPS:
        yield from group.iter_parameter_ids()
