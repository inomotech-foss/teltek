from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueMapping,
    ValueRange,
)

_UNPLUG_DETECTION = ParameterGroup(
    key="unplug_detection",
    name="Unplug Detection",
    parameters=[
        Parameter(
            key="scenario_setting",
            id=11500,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Scenario setting",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
        ),
        Parameter(
            key="eventual_records",
            id=11501,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(0, 1),
            name="Eventual records",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("ENABLE", 1, "Enable"),
            ],
        ),
        Parameter(
            key="detection_mode",
            id=11502,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(0, 1),
            name="Detection mode",
            value_map=[
                ValueMapping("SIMPLE", 0, "Simple"),
                ValueMapping("ADVANCED", 1, "Advanced"),
            ],
        ),
        Parameter(
            key="send_sms_to",
            id=7036,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8036,
            type=ParameterType.STRING,
            default_value="Unplug",
            value_range=ValueRange(0, 160),
            name="SMS Text",
        ),
    ],
)

_TOWING_DETECTION = ParameterGroup(
    key="towing_detection",
    name="Towing Detection",
    parameters=[
        Parameter(
            key="priority",
            id=11600,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Priority",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
        ),
        Parameter(
            key="eventual_records",
            id=11601,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(0, 1),
            name="Eventual records",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("ENABLE", 1, "Enable"),
            ],
        ),
        Parameter(
            key="activation_timeout",
            id=11602,
            type=ParameterType.U16,
            default_value=5,
            value_range=ValueRange(0, 65535),
            name="Activation timeout",
        ),
        Parameter(
            key="event_timeout",
            id=11603,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 60),
            name="Event timeout",
        ),
        Parameter(
            key="make_call_to",
            id=11604,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Make call to",
        ),
        Parameter(
            key="threshold",
            id=11605,
            type=ParameterType.DOUBLE,
            default_value=0.22,
            value_range=ValueRange(0.1, 5),
            name="Threshold",
        ),
        Parameter(
            key="angle",
            id=11606,
            type=ParameterType.DOUBLE,
            default_value=1,
            value_range=ValueRange(0.1, 5),
            name="Angle",
        ),
        Parameter(
            key="duration",
            id=11607,
            type=ParameterType.U16,
            default_value=1000,
            value_range=ValueRange(1, 5000),
            name="Duration",
        ),
        Parameter(
            key="send_sms_to",
            id=7035,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8035,
            type=ParameterType.STRING,
            default_value="Towing",
            value_range=ValueRange(0, 160),
            name="SMS Text",
        ),
    ],
)

_CRASH_DETECTION = ParameterGroup(
    key="crash_detection",
    name="Crash Detection",
    parameters=[
        Parameter(
            key="scenario_setting",
            id=11400,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Scenario setting",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
        ),
        Parameter(
            key="duration",
            id=11401,
            type=ParameterType.U8,
            default_value=5,
            value_range=ValueRange(0, 1000),
            name="Duration",
        ),
        Parameter(
            key="threshold",
            id=11402,
            type=ParameterType.U16,
            default_value=1500,
            value_range=ValueRange(0, 7900),
            name="Threshold",
        ),
        Parameter(
            key="crash_trace",
            id=11406,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 2),
            name="Crash trace",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("TRACE_CHANGES", 1, "Enable"),
                ValueMapping("TRACE_FULL", 2, "Trace full"),
            ],
        ),
        Parameter(
            key="send_sms_to",
            id=7037,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8037,
            type=ParameterType.STRING,
            default_value="Crash",
            value_range=ValueRange(0, 160),
            name="SMS Text",
        ),
    ],
)

_EXCESSIVE_IDLING = ParameterGroup(
    key="excessive_idling",
    name="Excessive Idling",
    parameters=[
        Parameter(
            key="scenario_settings",
            id=11200,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Scenario settings",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
        ),
        Parameter(
            key="eventual_records",
            id=11203,
            type=ParameterType.U8,
            default_value=1,
            value_range=ValueRange(0, 1),
            name="Eventual records",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("ENABLE", 1, "Enable"),
            ],
        ),
        Parameter(
            key="time_to_stopped",
            id=11205,
            type=ParameterType.U8,
            default_value=5,
            value_range=ValueRange(0, 3600),
            name="Time to stopped",
        ),
        Parameter(
            key="time_to_moving",
            id=11206,
            type=ParameterType.U8,
            default_value=2,
            value_range=ValueRange(0, 3600),
            name="Time to moving",
        ),
        Parameter(
            key="output_control",
            id=11204,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 2),
            name="Output control",
            value_map=[
                ValueMapping("NONE", 0, "None"),
                ValueMapping("DOUT1", 1, "DOUT 1"),
                ValueMapping("DOUT2", 2, "DOUT 2"),
            ],
        ),
        Parameter(
            key="dout_on_duration",
            id=11201,
            type=ParameterType.I32,
            default_value=200,
            value_range=ValueRange(0, 2147483647),
            name="DOUT ON Duration",
        ),
        Parameter(
            key="dout_off_duration",
            id=11202,
            type=ParameterType.I32,
            default_value=200,
            value_range=ValueRange(0, 2147483647),
            name="DOUT OFF Duration",
        ),
        Parameter(
            key="send_sms_to",
            id=7033,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8033,
            type=ParameterType.STRING,
            default_value="Idling Event",
            value_range=ValueRange(0, 160),
            name="SMS Text",
        ),
    ],
)

_MOTORCYCLE_FALL_DETECTION = ParameterGroup(
    key="motorcycle_fall_detection",
    name="Motorcycle Fall Detection",
    parameters=[
        Parameter(
            key="scenario_settings",
            id=13700,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Scenario settings",
            value_map=[
                ValueMapping("DISABLE", 0, "Disable"),
                ValueMapping("LOW_PRIORITY", 1, "Low priority"),
                ValueMapping("HIGH_PRIORITY", 2, "High priority"),
                ValueMapping("PANIC_PRIORITY", 3, "Panic priority"),
            ],
        ),
        Parameter(
            key="angle_value",
            id=13701,
            type=ParameterType.U8,
            default_value=45,
            value_range=ValueRange(30, 150),
            name="Angle value",
        ),
        Parameter(
            key="alarm_delay",
            id=13702,
            type=ParameterType.U8,
            default_value=5,
            value_range=ValueRange(0, 60),
            name="Alarm Delay",
        ),
        Parameter(
            key="active_time",
            id=13703,
            type=ParameterType.U16,
            default_value=15,
            value_range=ValueRange(0, 65500),
            name="Active Time",
        ),
        Parameter(
            key="output_control",
            id=13704,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 3),
            name="Output control",
            value_map=[
                ValueMapping("DISABLED", 0, "Disabled"),
                ValueMapping("DOUT1", 1, "DOUT 1"),
                ValueMapping("DOUT2", 2, "DOUT 2"),
            ],
        ),
        Parameter(
            key="dout_on_duration",
            id=13705,
            type=ParameterType.U32,
            default_value=200,
            value_range=ValueRange(100, 2147483647),
            name="DOUT ON Duration",
        ),
        Parameter(
            key="dout_off_duration",
            id=13706,
            type=ParameterType.U32,
            default_value=200,
            value_range=ValueRange(0, 2147483647),
            name="DOUT OFF Duration",
        ),
        Parameter(
            key="send_sms_to",
            id=7585,
            type=ParameterType.U8,
            default_value=0,
            value_range=ValueRange(0, 10),
            name="Send SMS to",
        ),
        Parameter(
            key="sms_text",
            id=8585,
            type=ParameterType.STRING,
            default_value="MotorcycleFallDetection",
            value_range=ValueRange(0, 160),
            name="SMS Text",
        ),
    ],
)

ACCELEROMETER = ParameterGroup(
    key="accelerometer",
    name="Accelerometer",
    groups=[
        _UNPLUG_DETECTION,
        _TOWING_DETECTION,
        _CRASH_DETECTION,
        _EXCESSIVE_IDLING,
        _MOTORCYCLE_FALL_DETECTION,
    ],
)