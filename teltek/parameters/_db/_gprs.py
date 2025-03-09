from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueMapping,
    ValueRange,
)

_PARAMETERS1: list[Parameter] = [
    Parameter(
        key="open_link_timeout",
        id=1000,
        type=ParameterType.U32,
        default_value=5,
        value_range=ValueRange(0, 259200),
        name="Open link timeout",
    ),
    Parameter(
        key="response_timeout",
        id=1001,
        type=ParameterType.U16,
        default_value=30,
        value_range=ValueRange(5, 300),
        name="Response timeout",
    ),
    Parameter(
        key="sort_by",
        id=1002,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 1),
        name="Sort by",
        value_map=[
            ValueMapping("NEWEST", 0, "Newest"),
            ValueMapping("OLDEST", 1, "Oldest"),
        ],
    ),
]
_PARAMETERS2: list[Parameter] = [
    Parameter(
        key="gprs_context",
        id=2000,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 1),
        name="GPRS context",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
    Parameter(
        key="apn",
        id=2001,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 32),
        name="APN",
    ),
    Parameter(
        key="apn_username",
        id=2002,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 32),
        name="APN username",
    ),
    Parameter(
        key="apn_password",
        id=2003,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 32),
        name="APN password",
    ),
    Parameter(
        key="auto_apn",
        id=2025,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 1),
        name="Auto APN",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
]
_PARAMETERS3: list[Parameter] = [
    Parameter(
        key="domain",
        id=2004,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 55),
        name="Domain",
    ),
    Parameter(
        key="port",
        id=2005,
        type=ParameterType.U16,
        default_value=0,
        value_range=ValueRange(0, 65535),
        name="Port",
    ),
    Parameter(
        key="protocol",
        id=2006,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 3),
        name="Protocol",
        value_map=[
            ValueMapping("TCP", 0, "TCP"),
            ValueMapping("UDP", 1, "UDP"),
            ValueMapping("MQTT", 3, "UDP"),
        ],
    ),
]
_PARAMETERS4: list[Parameter] = [
    Parameter(
        key="backup_server_mode",
        id=2010,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 2),
        name="Backup Server Mode",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("BACKUP", 1, "Backup"),
            ValueMapping("DUPLICATE", 2, "Duplicate"),
        ],
    ),
    Parameter(
        key="backup_server_domain",
        id=2007,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 55),
        name="Backup Server Domain",
    ),
    Parameter(
        key="backup_server_port",
        id=2008,
        type=ParameterType.U16,
        default_value=0,
        value_range=ValueRange(0, 65535),
        name="Backup Server Port",
    ),
    Parameter(
        key="backup_server_protocol",
        id=2009,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 1),
        name="Backup Server Protocol",
        value_map=[
            ValueMapping("TCP", 0, "TCP"),
            ValueMapping("UDP", 1, "UDP"),
        ],
    ),
]
_PARAMETERS5: list[Parameter] = [
    Parameter(
        key="fota_web_status",
        id=13003,
        type=ParameterType.U8,
        default_value=1,
        value_range=ValueRange(0, 1),
        name="FOTA WEB Status",
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
        ],
    ),
    Parameter(
        key="fota_web_domain",
        id=13000,
        type=ParameterType.STRING,
        default_value="fm.teltonika.lt",
        value_range=ValueRange(0, 55),
        name="FOTA WEB Domain",
    ),
    Parameter(
        key="fota_web_port",
        id=13001,
        type=ParameterType.U16,
        default_value=5000,
        value_range=ValueRange(0, 65535),
        name="FOTA WEB Port",
    ),
    Parameter(
        key="fota_web_period",
        id=13002,
        type=ParameterType.U16,
        default_value=720,
        value_range=ValueRange(30, 65535),
        name="FOTA WEB Period",
    ),
]

_MQTT_PARAMETERS: list[Parameter] = [
    Parameter(
        key="mqtt_data_topic",
        id=67100,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 255),  # TODO: unknown what the max is
        name="MQTT Data Topic",
    ),
    Parameter(
        key="mqtt_command_topic",
        id=67101,
        type=ParameterType.STRING,
        default_value="",
        value_range=ValueRange(0, 255),  # TODO: unknown what the max is
        name="MQTT Command Topic",
    ),
]

GPRS = ParameterGroup(
    key="gprs",
    name="GPRS",
    parameters=_PARAMETERS1
    + _PARAMETERS2
    + _PARAMETERS3
    + _PARAMETERS4
    + _PARAMETERS5
    + _MQTT_PARAMETERS,
)
