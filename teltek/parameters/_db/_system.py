from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueMapping,
    ValueRange,
)

_PARAMETERS1: list[Parameter] = [
    Parameter(
        key="movement_source",
        id=138,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 2),
        name="Movement source",
        value_map=[
            ValueMapping("IGNITION", 1, "Ignition"),
            ValueMapping("MOVEMENT", 2, "Movement"),
            ValueMapping("GPS", 4, "GPS"),
        ],
    ),
    Parameter(
        key="static_navigation",
        id=106,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 1),
        name="Static navigation",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
    Parameter(
        key="static_navigation_src",
        id=112,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 3),
        name="Static navigation source",
        value_map=[
            ValueMapping("MOVEMENT", 1, "Movement"),
            ValueMapping("IGNITION", 2, "Ignition"),
            ValueMapping("MOVEMENT_AND_IGNITION", 3, "Movement and Ignition"),
        ],
    ),
    Parameter(
        key="records_without_ts",
        id=107,
        type=ParameterType.U8,
        default_value=2,
        value_range=ValueRange(0, 2),
        name="Send/Save records without TS",
        value_map=[
            ValueMapping("AFTER_POSITION_FIX", 0, "After Position Fix"),
            ValueMapping("ALWAYS", 1, "Always"),
            ValueMapping("AFTER_TIME_SYNC", 2, "After Time Sync"),
        ],
    ),
    Parameter(
        key="led_indication",
        id=108,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 1),
        name="LED Indication",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
    Parameter(
        key="gnss_source",
        id=109,
        type=ParameterType.U8,
        default_value=10,
        value_range=ValueRange(1, 15),
        name="GNSS source",
        value_map=[
            ValueMapping("BEIDOU_ONLY", 1, "Beidou only"),
            ValueMapping("GLONASS_ONLY", 2, "Glonass only"),
            ValueMapping(
                "GLONASS_BEIDOU_NOT_ALLOWED", 3, "Glonass and Beidou not allowed"
            ),
            ValueMapping("GALILEO_ONLY", 4, "Galileo only"),
            ValueMapping("GALILEO_BEIDOU", 5, "Galileo and Beidou"),
            ValueMapping("GALILEO_GLONASS", 6, "Galileo and Glonass"),
            ValueMapping(
                "GALILEO_GLONASS_BEIDOU_NOT_ALLOWED",
                7,
                "Galileo, Glonass and Beidou not allowed",
            ),
            ValueMapping("GPS_ONLY", 8, "Gps only"),
            ValueMapping("GPS_BEIDOU", 9, "Gps and Beidou"),
            ValueMapping("GPS_GLONASS", 10, "Gps and Glonass"),
            ValueMapping(
                "GPS_GLONASS_BEIDOU_NOT_ALLOWED",
                11,
                "Gps, Glonass and Beidou not allowed",
            ),
            ValueMapping("GPS_GALILEO", 12, "Gps and Galileo"),
            ValueMapping("GPS_GALILEO_BEIDOU", 13, "Gps, Galileo and Beidou"),
            ValueMapping("GPS_GALILEO_GLONASS", 14, "Gps, Galileo and Glonass"),
            ValueMapping(
                "GPS_GALILEO_GLONASS_BEIDOU_NOT_ALLOWED",
                15,
                "Gps, Galileo, Glonass and Beidou and not allowed",
            ),
        ],
    ),
    Parameter(
        key="battery_charge_mode",
        id=110,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 1),
        name="Battery charge mode",
        value_map=[
            ValueMapping("ON_NEED", 0, "On need"),
            ValueMapping("AFTER_IGNITION_ON", 1, "After ignition on"),
        ],
    ),
    Parameter(
        key="protocol_settings",
        id=113,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 4),
        name="Protocol Settings",
        value_map=[
            ValueMapping("CODEC_8", 0, "Codec 8"),
            ValueMapping("CODEC_8_EXT", 1, "Codec 8 Extended"),
            ValueMapping("CODEC_AWS_JSON", 4, "Codec AWS JSON"),
        ],
    ),
]
_PARAMETERS2: list[Parameter] = [
    Parameter(
        key="sleep_settings",
        id=102,
        type=ParameterType.U8,
        default_value=2,
        value_range=ValueRange(0, 2),
        name="Sleep settings",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("GPS_SLEEP", 1, "Gps sleep"),
            ValueMapping("DEEP_SLEEP", 2, "Deep sleep"),
            ValueMapping("ONLINE_DEEP_SLEEP", 3, "Online Deep sleep"),
            ValueMapping("ULTRA_SLEEP", 4, "Ultra sleep"),
        ],
    ),
    Parameter(
        key="timeout",
        id=103,
        type=ParameterType.U16,
        default_value=1,
        value_range=ValueRange(1, 3000),
        name="Timeout",
    ),
]
_PARAMETERS3: list[Parameter] = [
    Parameter(
        key="ignition_settings",
        id=101,
        type=ParameterType.U8,
        default_value=4,
        value_range=ValueRange(1, 14),
        name="Ignition settings",
        value_map=[
            ValueMapping("ACCELEROMETER", 1, "Accelerometer"),
            ValueMapping(
                "DIGITAL_INPUT_OR_ACCELEROMETER", 3, "Digital Input or Accelerometer"
            ),
            ValueMapping("POWER_VOLTAGE", 4, "Power Voltage"),
            ValueMapping(
                "DIGITAL_INPUT_OR_POWER_VOLTAGE", 5, "Digital Input or Power Voltage"
            ),
            ValueMapping(
                "ACCELEROMETER_OR_POWER_VOLTAGE", 6, "Accelerometer or Power Voltage"
            ),
            ValueMapping(
                "DIGITAL_INPUT_ACCELEROMETER_POWER_VOLTAGE",
                7,
                "Digital Input, Accelerometer, or Power Voltage",
            ),
            ValueMapping("ENGINE_RPM", 8, "Engine RPM"),
            ValueMapping(
                "DIGITAL_INPUT_OR_ENGINE_RPM", 9, "Digital Input or Engine RPM"
            ),
            ValueMapping(
                "ACCELEROMETER_OR_ENGINE_RPM", 10, "Accelerometer or Engine RPM"
            ),
            ValueMapping(
                "DIGITAL_INPUT_ACCELEROMETER_ENGINE_RPM",
                11,
                "Digital Input, Accelerometer or Engine RPM",
            ),
            ValueMapping(
                "POWER_VOLTAGE_OR_ENGINE_RPM", 12, "Power Voltage or Engine RPM"
            ),
            ValueMapping(
                "DIGITAL_INPUT_POWER_VOLTAGE_ENGINE_RPM",
                13,
                "Digital Input, Power Voltage or Engine RPM",
            ),
            ValueMapping(
                "ACCELEROMETER_POWER_VOLTAGE_ENGINE_RPM",
                14,
                "Accelerometer, Power Voltage or Engine RPM",
            ),
        ],
    ),
    Parameter(
        key="high_voltage",
        id=104,
        type=ParameterType.U16,
        default_value=30000,
        value_range=ValueRange(0, 30000),
        name="High voltage",
    ),
    Parameter(
        key="low_voltage",
        id=105,
        type=ParameterType.U16,
        default_value=13200,
        value_range=ValueRange(0, 29999),
        name="Low voltage",
    ),
]
_PARAMETERS4: list[Parameter] = [
    Parameter(
        key="movement_start_delay",
        id=19001,
        type=ParameterType.U16,
        default_value=5,
        value_range=ValueRange(1, 60),
        name="Movement Start Delay",
    ),
    Parameter(
        key="movement_stop_delay",
        id=19002,
        type=ParameterType.U16,
        default_value=60,
        value_range=ValueRange(5, 300),
        name="Movement Stop Delay",
    ),
]
_PARAMETERS5: list[Parameter] = [
    Parameter(
        key="sync_settings",
        id=900,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 3),
        name="Synchronization settings",
        value_map=[
            ValueMapping("GPS_ONLY", 1, "Gps only"),
            ValueMapping("NITZ_NTP", 2, "NITZ and NTP"),
            ValueMapping("NTP", 3, "NTP"),
        ],
    ),
    Parameter(
        key="ntp_resync",
        id=901,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 24),
        name="NTP Resync",
    ),
    Parameter(
        key="ntp_server1",
        id=902,
        type=ParameterType.STRING,
        default_value="avl1.teltonika.lt",
        value_range=ValueRange(0, 55),
        name="NTP server 1",
    ),
    Parameter(
        key="ntp_server2",
        id=903,
        type=ParameterType.STRING,
        default_value="pool.ntp.org",
        value_range=ValueRange(0, 55),
        name="NTP server 2",
    ),
]
_PARAMETERS6: list[Parameter] = [
    Parameter(
        key="accel_auto_calib",
        id=169,
        type=ParameterType.U8,
        default_value=2,
        value_range=ValueRange(0, 2),
        name="Accelerometer Auto Calibration",
        value_map=[
            ValueMapping("DISABLED", 0, "Disabled"),
            ValueMapping("ONCE", 1, "Once"),
            ValueMapping("CONTINUOUS", 2, "Continuous"),
        ],
    ),
    Parameter(
        key="gravity_filter",
        id=170,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 1),
        name="Gravity Filter",
        value_map=[
            ValueMapping("DISABLED", 0, "Disabled"),
            ValueMapping("ENABLED", 1, "Enabled"),
        ],
    ),
]

SYSTEM = ParameterGroup(
    key="system",
    name="System",
    parameters=_PARAMETERS1
    + _PARAMETERS2
    + _PARAMETERS3
    + _PARAMETERS4
    + _PARAMETERS5
    + _PARAMETERS6,
)
