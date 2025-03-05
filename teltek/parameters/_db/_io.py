from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueMapping,
    ValueRange,
)


def priority(id: int, *, default_value: int) -> Parameter:
    return Parameter(
        key="priority",
        id=id,
        type=ParameterType.U8,
        default_value=default_value,
        value_range=ValueRange(0, 3),
        value_map=[
            ValueMapping("DISABLED", 0, "Disabled"),
            ValueMapping("LOW", 1, "Low"),
            ValueMapping("HIGH", 2, "High"),
            ValueMapping("PANIC", 3, "Panic"),
        ],
        name="Priority",
    )


def operand(id: int, *, default_value: int) -> Parameter:
    return Parameter(
        key="operand",
        id=id,
        type=ParameterType.U8,
        default_value=default_value,
        value_range=ValueRange(0, 6),
        value_map=[
            ValueMapping("ON_RANGE_EXIT", 0, "On range exit"),
            ValueMapping("ON_RANGE_ENTRANCE", 1, "On range entrance"),
            ValueMapping("ON_BOTH", 2, "On both"),
            ValueMapping("MONITORING", 3, "Monitoring"),
            ValueMapping("HYSTERESIS", 4, "Hysteresis"),
            ValueMapping("ON_CHANGE", 5, "On change"),
            ValueMapping("ON_DELTA_CHANGE", 6, "On delta change"),
        ],
        name="Operand",
    )


def high_level(
    id: int,
    *,
    type: ParameterType,
    default_value: int,
    min: int,
    max: int,
) -> Parameter:
    return Parameter(
        key="high_level",
        id=id,
        type=type,
        default_value=default_value,
        value_range=ValueRange(min, max),
        value_map=None,
        name="High level",
    )


def low_level(
    id: int,
    *,
    type: ParameterType,
    default_value: int,
    min: int,
    max: int,
) -> Parameter:
    return Parameter(
        key="low_level",
        id=id,
        type=type,
        default_value=default_value,
        value_range=ValueRange(min, max),
        value_map=None,
        name="Low level",
    )


def event_only(id: int) -> Parameter:
    return Parameter(
        key="event_only",
        id=id,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 2),
        value_map=[
            ValueMapping("DISABLE", 0, "Disable"),
            ValueMapping("ENABLE", 1, "Enable"),
            ValueMapping("CRASH", 2, "Crash"),
        ],
        name="Event only",
    )


def _average(id: int, *, default_value: int) -> Parameter:
    return Parameter(
        key="average",
        id=id,
        type=ParameterType.U16,
        default_value=default_value,
        value_range=ValueRange(0, 65535),
        value_map=None,
        name="Average",
    )


def send_sms_to(id: int) -> Parameter:
    return Parameter(
        key="send_sms_to",
        id=id,
        type=ParameterType.U8,
        default_value=0,
        value_range=ValueRange(0, 10),
        value_map=None,
        name="Send SMS to",
    )


def sms_text(id: int, *, default_value: str) -> Parameter:
    return Parameter(
        key="sms_text",
        id=id,
        type=ParameterType.STRING,
        default_value=default_value,
        value_range=ValueRange(0, 160),
        value_map=None,
        name="SMS text",
    )


_IGNITION = ParameterGroup(
    key="ignition",
    name="Ignition",
    parameters=[
        priority(50000, default_value=1),
        operand(50001, default_value=5),
        high_level(50002, type=ParameterType.U8, default_value=0, min=0, max=1),
        low_level(50003, type=ParameterType.U8, default_value=0, min=0, max=1),
        event_only(50004),
        _average(50005, default_value=10),
        send_sms_to(7000),
        sms_text(8000, default_value="Ignition"),
    ],
)

_MOVEMENT = ParameterGroup(
    key="movement",
    name="Movement",
    parameters=[
        priority(50010, default_value=1),
        operand(50011, default_value=5),
        high_level(50012, type=ParameterType.U8, default_value=0, min=0, max=1),
        low_level(50013, type=ParameterType.U8, default_value=0, min=0, max=1),
        event_only(50014),
        _average(50015, default_value=1),
        send_sms_to(7001),
        sms_text(8001, default_value="Movement"),
    ],
)

_DATA_MODE = ParameterGroup(
    key="data_mode",
    name="Data Mode",
    parameters=[
        priority(50020, default_value=1),
        operand(50021, default_value=3),
        high_level(50022, type=ParameterType.U8, default_value=0, min=0, max=5),
        low_level(50023, type=ParameterType.U8, default_value=0, min=0, max=5),
        event_only(50024),
        send_sms_to(7002),
        sms_text(8002, default_value="Data Mode"),
    ],
)

_GSM_SIGNAL = ParameterGroup(
    key="gsm_signal",
    name="GSM Signal",
    parameters=[
        priority(50030, default_value=1),
        operand(50031, default_value=3),
        high_level(50032, type=ParameterType.U8, default_value=0, min=0, max=5),
        low_level(50033, type=ParameterType.U8, default_value=0, min=0, max=5),
        event_only(50034),
        _average(50035, default_value=1),
        send_sms_to(7003),
        sms_text(8003, default_value="GSM Signal"),
    ],
)

_SLEEP = ParameterGroup(
    key="sleep",
    name="Sleep",
    parameters=[
        priority(50040, default_value=1),
        operand(50041, default_value=3),
        high_level(50042, type=ParameterType.U8, default_value=0, min=0, max=2),
        low_level(50043, type=ParameterType.U8, default_value=0, min=0, max=2),
        event_only(50044),
        send_sms_to(7004),
        sms_text(8004, default_value="Sleep"),
    ],
)

_GNSS_STATUS = ParameterGroup(
    key="gnss_status",
    name="GNSS Status",
    parameters=[
        priority(50050, default_value=1),
        operand(50051, default_value=3),
        high_level(50052, type=ParameterType.U8, default_value=0, min=0, max=5),
        low_level(50053, type=ParameterType.U8, default_value=0, min=0, max=5),
        event_only(50053),
        send_sms_to(7005),
        sms_text(8005, default_value="GNSS Status"),
    ],
)

_GNSS_PDOP = ParameterGroup(
    key="gnss_pdop",
    name="GNSS PDOP",
    parameters=[
        priority(50060, default_value=0),
        operand(5061, default_value=3),
        high_level(5062, type=ParameterType.U16, default_value=0, min=0, max=1000),
        low_level(5063, type=ParameterType.U16, default_value=0, min=0, max=1000),
        event_only(5064),
        _average(5065, default_value=10),
        send_sms_to(7006),
        sms_text(8006, default_value="GNSS PDOP"),
    ],
)

_GNSS_HDOP = ParameterGroup(
    key="gnss_hdop",
    name="GNSS HDOP",
    parameters=[
        priority(50070, default_value=1),
        operand(50071, default_value=3),
        high_level(50072, type=ParameterType.U16, default_value=0, min=0, max=1000),
        low_level(50073, type=ParameterType.U16, default_value=0, min=0, max=1000),
        event_only(50074),
        _average(50075, default_value=10),
        send_sms_to(7007),
        sms_text(8007, default_value="GNSS HDOP"),
    ],
)

_EXTERNAL_VOLTAGE = ParameterGroup(
    key="external_voltage",
    name="External Voltage",
    parameters=[
        priority(50080, default_value=1),
        operand(50081, default_value=6),
        high_level(50082, type=ParameterType.U16, default_value=1000, min=0, max=60000),
        low_level(50083, type=ParameterType.U16, default_value=0, min=0, max=60000),
        event_only(50084),
        _average(50085, default_value=10),
        send_sms_to(7008),
        sms_text(8008, default_value="External Voltage"),
    ],
)

_SPEED = ParameterGroup(
    key="speed",
    name="Speed",
    parameters=[
        priority(50090, default_value=1),
        operand(50091, default_value=3),
        high_level(50092, type=ParameterType.U16, default_value=0, min=0, max=300),
        low_level(50093, type=ParameterType.U16, default_value=0, min=0, max=300),
        event_only(50094),
        _average(50095, default_value=1),
        send_sms_to(7009),
        sms_text(8009, default_value="Speed"),
    ],
)

_GSM_CELL_ID = ParameterGroup(
    key="gsm_cell_id",
    name="GSM Cell ID",
    parameters=[
        priority(50100, default_value=0),
        operand(50101, default_value=3),
        high_level(50102, type=ParameterType.U32, default_value=0, min=0, max=999999),
        low_level(50103, type=ParameterType.U32, default_value=0, min=0, max=999999),
        event_only(50104),
        send_sms_to(7010),
        sms_text(8010, default_value="GSM Cell ID"),
    ],
)

_GSM_AREA_CODE = ParameterGroup(
    key="gsm_area_code",
    name="GSM Area Code",
    parameters=[
        priority(50110, default_value=0),
        operand(50111, default_value=3),
        high_level(50112, type=ParameterType.U32, default_value=0, min=0, max=999999),
        low_level(50113, type=ParameterType.U32, default_value=0, min=0, max=999999),
        event_only(50114),
        send_sms_to(7011),
        sms_text(8011, default_value="GSM Area Code"),
    ],
)

_BATTERY_VOLTAGE = ParameterGroup(
    key="battery_voltage",
    name="Battery Voltage",
    parameters=[
        priority(50120, default_value=1),
        operand(50121, default_value=3),
        high_level(50122, type=ParameterType.U16, default_value=0, min=0, max=5000),
        low_level(50123, type=ParameterType.U16, default_value=0, min=0, max=5000),
        event_only(50124),
        _average(50125, default_value=0),
        send_sms_to(7012),
        sms_text(8012, default_value="Battery Voltage"),
    ],
)

_BATTERY_CURRENT = ParameterGroup(
    key="battery_current",
    name="Battery Current",
    parameters=[
        priority(50130, default_value=1),
        operand(50131, default_value=3),
        high_level(50132, type=ParameterType.U16, default_value=0, min=0, max=5000),
        low_level(50133, type=ParameterType.U16, default_value=0, min=0, max=5000),
        event_only(50134),
        _average(50135, default_value=0),
        send_sms_to(7013),
        sms_text(8013, default_value="Battery Current"),
    ],
)

_ACTIVE_GSM_OPERATOR = ParameterGroup(
    key="active_gsm_operator",
    name="Active GSM Operator",
    parameters=[
        priority(50140, default_value=0),
        operand(50141, default_value=3),
        high_level(50142, type=ParameterType.U32, default_value=0, min=0, max=999999),
        low_level(50143, type=ParameterType.U32, default_value=0, min=0, max=999999),
        event_only(50144),
        send_sms_to(7014),
        sms_text(8014, default_value="Active GSM Operator"),
    ],
)

_TRIP_ODOMETER = ParameterGroup(
    key="trip_odometer",
    name="Trip Odometer",
    parameters=[
        priority(50150, default_value=0),
        operand(50151, default_value=3),
        high_level(50152, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        low_level(50153, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        event_only(50154),
        send_sms_to(7015),
        sms_text(8015, default_value="Trip Odometer"),
    ],
)

_TOTAL_ODOMETER = ParameterGroup(
    key="total_odometer",
    name="Total Odometer",
    parameters=[
        priority(50160, default_value=0),
        operand(50161, default_value=3),
        high_level(50162, type=ParameterType.U32, default_value=0, min=0, max=10000000),
        low_level(50163, type=ParameterType.U32, default_value=0, min=0, max=10000000),
        event_only(50164),
        send_sms_to(7016),
        sms_text(8016, default_value="Total Odometer"),
    ],
)

_FUEL_USED_GPS = ParameterGroup(
    key="fuel_used_gps",
    name="Fuel Used GPS",
    parameters=[
        priority(50200, default_value=0),
        operand(50201, default_value=3),
        high_level(50202, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        low_level(50203, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        event_only(50204),
        _average(50205, default_value=1),
        send_sms_to(7020),
        sms_text(8020, default_value="Fuel Used GPS"),
    ],
)

_FUEL_RATE_GPS = ParameterGroup(
    key="fuel_rate_gps",
    name="Fuel Rate GPS",
    parameters=[
        priority(50210, default_value=0),
        operand(50211, default_value=3),
        high_level(50212, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        low_level(50213, type=ParameterType.U32, default_value=0, min=0, max=1000000),
        event_only(50214),
        _average(50215, default_value=1),
        send_sms_to(7021),
        sms_text(8021, default_value="Fuel Rate GPS"),
    ],
)

_AXIS_X = ParameterGroup(
    key="axis_x",
    name="Axis X",
    parameters=[
        priority(50220, default_value=0),
        operand(50221, default_value=3),
        high_level(50222, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        low_level(50223, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        event_only(50224),
        _average(50225, default_value=1),
        send_sms_to(7022),
        sms_text(8022, default_value="Axis X"),
    ],
)

_AXIS_Y = ParameterGroup(
    key="axis_y",
    name="Axis Y",
    parameters=[
        priority(50230, default_value=0),
        operand(50231, default_value=3),
        high_level(50232, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        low_level(50233, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        event_only(50234),
        _average(50235, default_value=1),
        send_sms_to(7023),
        sms_text(8023, default_value="Axis Y"),
    ],
)

_AXIS_Z = ParameterGroup(
    key="axis_z",
    name="Axis Z",
    parameters=[
        priority(50240, default_value=0),
        operand(50241, default_value=3),
        high_level(50242, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        low_level(50243, type=ParameterType.U16, default_value=0, min=-8000, max=8000),
        event_only(50244),
        _average(50245, default_value=1),
        send_sms_to(7024),
        sms_text(8024, default_value="Axis Z"),
    ],
)

_ICCID = ParameterGroup(
    key="iccid",
    name="ICCID",
    parameters=[
        priority(50250, default_value=0),
        operand(50251, default_value=3),
        event_only(50254),
        send_sms_to(7069),
        sms_text(8069, default_value="ICCID"),
    ],
)

_ECO_SCORE = ParameterGroup(
    key="eco_score",
    name="Eco Score",
    parameters=[
        priority(50510, default_value=0),
        operand(50511, default_value=3),
        high_level(50512, type=ParameterType.U8, default_value=0, min=0, max=1),
        low_level(50513, type=ParameterType.U8, default_value=0, min=0, max=1),
        event_only(50514),
        send_sms_to(7220),
        sms_text(8220, default_value="Eco Score"),
    ],
)

_BATTERY_LEVEL = ParameterGroup(
    key="battery_level",
    name="Battery Level",
    parameters=[
        priority(50690, default_value=0),
        operand(50691, default_value=0),
        high_level(50692, type=ParameterType.U8, default_value=0, min=0, max=100),
        low_level(50693, type=ParameterType.U8, default_value=0, min=0, max=100),
        event_only(50694),
        _average(50695, default_value=1),
        send_sms_to(7243),
        sms_text(8243, default_value="Battery Level"),
    ],
)

_BT_STATUS = ParameterGroup(
    key="bt_status",
    name="BT Status",
    parameters=[
        priority(50720, default_value=0),
        operand(50721, default_value=5),
        high_level(50722, type=ParameterType.U8, default_value=0, min=0, max=4),
        low_level(50723, type=ParameterType.U8, default_value=0, min=0, max=3),
        event_only(50724),
        _average(50725, default_value=1),
        send_sms_to(7250),
        sms_text(8250, default_value="BT Status"),
    ],
)


IO = ParameterGroup(
    key="io",
    name="I/O",
    groups=[
        _IGNITION,
        _MOVEMENT,
        _DATA_MODE,
        _GSM_SIGNAL,
        _SLEEP,
        _GNSS_STATUS,
        _GNSS_PDOP,
        _GNSS_HDOP,
        _EXTERNAL_VOLTAGE,
        _SPEED,
        _GSM_CELL_ID,
        _GSM_AREA_CODE,
        _BATTERY_VOLTAGE,
        _BATTERY_CURRENT,
        _ACTIVE_GSM_OPERATOR,
        _TRIP_ODOMETER,
        _TOTAL_ODOMETER,
        _FUEL_USED_GPS,
        _FUEL_RATE_GPS,
        _AXIS_X,
        _AXIS_Y,
        _AXIS_Z,
        _ICCID,
        _ECO_SCORE,
        _BATTERY_LEVEL,
        _BT_STATUS,
    ],
)
