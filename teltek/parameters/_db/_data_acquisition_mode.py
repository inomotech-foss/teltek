from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueRange,
)

_HOME_STOP = ParameterGroup(
    key="home_stop",
    name='Home Network GSM operator code "Vehicle on STOP"',
    parameters=[
        Parameter(
            key="min_period",
            id=10000,
            type=ParameterType.U16,
            default_value=3600,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_saved_records",
            id=10004,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10005,
            type=ParameterType.U16,
            default_value=120,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)

_HOME_MOVING = ParameterGroup(
    key="home_moving",
    name='Home Network GSM operator code "Vehicle MOVING"',
    parameters=[
        Parameter(
            key="min_period",
            id=10050,
            type=ParameterType.U16,
            default_value=300,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_distance",
            id=10051,
            type=ParameterType.U16,
            default_value=100,
            value_range=ValueRange(0, 65535),
            name="Min Distance",
        ),
        Parameter(
            key="min_angle",
            id=10052,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 180),
            name="Min Angle",
        ),
        Parameter(
            key="min_speed_delta",
            id=10053,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 100),
            name="Min Speed Delta",
        ),
        Parameter(
            key="min_saved_records",
            id=10054,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10055,
            type=ParameterType.U16,
            default_value=120,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)

_ROAMING_STOP = ParameterGroup(
    key="roaming_stop",
    name='Roaming Network GSM operator code "Vehicle on STOP"',
    parameters=[
        Parameter(
            key="min_period",
            id=10100,
            type=ParameterType.U16,
            default_value=3600,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_saved_records",
            id=10104,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10105,
            type=ParameterType.U16,
            default_value=0,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)
_ROAMING_MOVING = ParameterGroup(
    key="roaming_moving",
    name='Roaming Network GSM operator code "Vehicle MOVING"',
    parameters=[
        Parameter(
            key="min_period",
            id=10150,
            type=ParameterType.U16,
            default_value=300,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_distance",
            id=10151,
            type=ParameterType.U16,
            default_value=100,
            value_range=ValueRange(0, 65535),
            name="Min Distance",
        ),
        Parameter(
            key="min_angle",
            id=10152,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 180),
            name="Min Angle",
        ),
        Parameter(
            key="min_speed_delta",
            id=10153,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 100),
            name="Min Speed Delta",
        ),
        Parameter(
            key="min_saved_records",
            id=10154,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10155,
            type=ParameterType.U16,
            default_value=0,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)

_UNKNOWN_STOP = ParameterGroup(
    key="unknown_stop",
    name='Unknown Network GSM operator code "Vehicle on STOP"',
    parameters=[
        Parameter(
            key="min_period",
            id=10200,
            type=ParameterType.U16,
            default_value=3600,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_saved_records",
            id=10204,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10205,
            type=ParameterType.U16,
            default_value=120,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)

_UNKNOWN_MOVING = ParameterGroup(
    key="unknown_moving",
    name='Unknown Network GSM operator code "Vehicle MOVING"',
    parameters=[
        Parameter(
            key="min_period",
            id=10250,
            type=ParameterType.U16,
            default_value=300,
            value_range=ValueRange(0, 65535),
            name="Min Period",
        ),
        Parameter(
            key="min_distance",
            id=10251,
            type=ParameterType.U16,
            default_value=100,
            value_range=ValueRange(0, 65535),
            name="Min Distance",
        ),
        Parameter(
            key="min_angle",
            id=10252,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 180),
            name="Min Angle",
        ),
        Parameter(
            key="min_speed_delta",
            id=10253,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(0, 100),
            name="Min Speed Delta",
        ),
        Parameter(
            key="min_saved_records",
            id=10254,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(1, 255),
            name="Min Saved Records",
        ),
        Parameter(
            key="send_period",
            id=10255,
            type=ParameterType.U16,
            default_value=0,
            value_range=ValueRange(0, 65535),
            name="Send Period",
        ),
    ],
)

DATA_ACQUISITION_MODE = ParameterGroup(
    key="data_acquisition_mode",
    name="Data acquisition mode",
    groups=[
        _HOME_STOP,
        _HOME_MOVING,
        _ROAMING_STOP,
        _ROAMING_MOVING,
        _UNKNOWN_STOP,
        _UNKNOWN_MOVING,
    ],
)
