from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueMapping,
    ValueRange,
)

_TRIP_SCENARIO = ParameterGroup(
    key="trip_scenario",
    name="Trip Scenario",
    parameters=[
        Parameter(
            key="scenario_settings",
            id=11800,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
            name="Scenario settings",
        ),
        Parameter(
            key="eventual_records",
            id=11801,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(0, 1),
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("ENABLE", 1, "Enable"),
            ],
            name="Eventual records",
        ),
        Parameter(
            key="mode",
            id=11802,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 1),
            value_map=[
                ValueMapping("CONTINUOUS", 0, "Continuous"),
                ValueMapping("BETWEEN_RECORDS", 1, "Between records"),
            ],
            name="Mode",
        ),
        Parameter(
            key="start_speed",
            id=11803,
            type=ParameterType.U8,
            default_value=5,
            value_range=ValueRange(0, 255),
            name="Start speed",
        ),
        Parameter(
            key="ignition_off_timeout",
            id=11804,
            type=ParameterType.U16,
            default_value=60,
            value_range=ValueRange(0, 65535),
            name="Ignition off timeout",
        ),
        Parameter(
            key="send_sms_to",
            id=7031,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8031,
            type=ParameterType.STRING,
            default_value="Trip",
            value_range=ValueRange(0, 160),
            name="Sms text",
        ),
    ],
)

_ADVANCED_TRIP_SCENARIO = ParameterGroup(
    key="advanced_trip_scenario",
    name="Advanced Trip Scenario",
    parameters=[
        Parameter(
            key="eco_score_allowed_events",
            id=700,
            type=ParameterType.U16,
            default_value=100,
            value_range=ValueRange(0, 65535),
            name="Eco score allowed events",
        ),
        Parameter(
            key="remember_ibutton",
            id=11805,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 1),
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("ENABLE", 1, "Enable"),
            ],
            name="Remember iButton",
        ),
    ],
)

_ODOMETER = ParameterGroup(
    key="odometer",
    name="Odometer",
    parameters=[
        Parameter(
            key="calculation_source",
            id=11806,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 2),
            value_map=[
                ValueMapping("GNSS", 0, "GNSS"),
                ValueMapping("OBD", 1, "OBD"),
                ValueMapping("LVCAN", 2, "LVCAN"),
            ],
            name="Calculation source",
        ),
        Parameter(
            key="value",
            id=11807,
            type=ParameterType.U32,
            default_value=0,
            value_range=ValueRange(0, 4294967),
            name="Odometer Value",
        ),
    ],
)

TRIP_ODOMETER = ParameterGroup(
    key="trip_odometer",
    name="Trip/Odometer",
    groups=[
        _TRIP_SCENARIO,
        _ADVANCED_TRIP_SCENARIO,
        _ODOMETER,
    ],
)
