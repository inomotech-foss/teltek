from ._parameter import (
    Parameter,
    ParameterGroup,
    ParameterIdRange,
    ParameterType,
    ValueMapping,
    ValueRange,
)

_PARAMETERS1: list[Parameter] = [
    Parameter(
        key="allow_sms_data_sending",
        id=3000,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 1),
        name="Allow SMS data sending",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
    Parameter(
        key="data_send_number",
        id=3001,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 16),
        name="Data Send Number",
    ),
]


_PARAMETERS2: list[Parameter] = [
    Parameter(
        key="login",
        id=3003,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 5),
        name="Login",
    ),
    Parameter(
        key="password",
        id=3004,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 5),
        name="Password",
    ),
    Parameter(
        key="sms_event_time_zone",
        id=3006,
        type=ParameterType.U16,  # TODO: is this true?
        default_value="UTC+00:00",
        value_range=ValueRange(
            "UTC-12:00",
            "UTC+13:00",
        ),
        name="SMS event Time Zone",
    ),
]

_PARAMETERS3: list[Parameter] = [
    Parameter(
        key="incoming_call_action",
        id=3005,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 4),
        name="Incoming call action",
        value_map=[
            ValueMapping("DO_NOTHING", 0, "Do nothing"),
            ValueMapping("HANGUP", 1, "Hangup"),
            ValueMapping("REPORT_POSITION", 2, "Report position"),
        ],
    ),
]

_PARAMETERS4: list[Parameter] = [
    Parameter(
        key="authorized_number",
        id=ParameterIdRange(4000, 4199),
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 16),
        name="Authorized number",
    ),
]

_PARAMETERS5: list[Parameter] = [
    Parameter(
        key="predefined_number",
        id=ParameterIdRange(6000, 6009),
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 16),
        name="Predefined number",
    ),
]

SMS = ParameterGroup(
    key="sms",
    name="SMS/Call",
    parameters=_PARAMETERS1 + _PARAMETERS2 + _PARAMETERS3 + _PARAMETERS4 + _PARAMETERS5,
)
