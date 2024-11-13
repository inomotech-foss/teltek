import functools

from teltek.parameters._db._io import (
    event_only,
    high_level,
    low_level,
    operand,
    priority,
    send_sms_to,
    sms_text,
)
from teltek.parameters._parameter import ParameterGroup, ParameterType

priority = functools.partial(priority, default_value=0)
operand = functools.partial(operand, default_value=3)
high_level = functools.partial(
    high_level, type=ParameterType.U8, default_value=0, min=0, max=255
)
low_level = functools.partial(
    low_level, type=ParameterType.U8, default_value=0, min=0, max=255
)


_NUMBER_OF_DTC = ParameterGroup(
    key="number_of_dtc",
    name="Number Of DTC",
    parameters=[
        priority(40100),
        low_level(40103),
        high_level(40102),
        event_only(40104),
        operand(40101),
        send_sms_to(7038),
        sms_text(8038, default_value="Number Of DTC"),
    ],
)
_ENGINE_LOAD = ParameterGroup(
    key="engine_load",
    name="Engine Load",
    parameters=[
        priority(40110),
        low_level(40113),
        high_level(40112),
        event_only(40114),
        operand(40111),
        send_sms_to(7039),
        sms_text(8039, default_value="Engine Load"),
    ],
)
_COOLANT_TEMPERATURE = ParameterGroup(
    key="coolant_temperature",
    name="Coolant Temperature",
    parameters=[
        priority(40120),
        low_level(40123),
        high_level(40122),
        event_only(40124),
        operand(40121),
        send_sms_to(7040),
        sms_text(8040, default_value="Coolant Temperature"),
    ],
)
_SHORT_FUEL_TRIM = ParameterGroup(
    key="short_fuel_trim",
    name="Short Fuel Trim",
    parameters=[
        priority(40130),
        low_level(40133),
        high_level(40132),
        event_only(40134),
        operand(40131),
        send_sms_to(7041),
        sms_text(8041, default_value="Short Fuel Trim"),
    ],
)
_FUEL_PRESSURE = ParameterGroup(
    key="fuel_pressure",
    name="Fuel Pressure",
    parameters=[
        priority(40140),
        low_level(40143),
        high_level(40142),
        event_only(40144),
        operand(40141),
        send_sms_to(7042),
        sms_text(8042, default_value="Fuel Pressure"),
    ],
)
_INTAKE_MAP = ParameterGroup(
    key="intake_map",
    name="Intake Map",
    parameters=[
        priority(40150),
        low_level(40153),
        high_level(40152),
        event_only(40154),
        operand(40151),
        send_sms_to(7043),
        sms_text(8043, default_value="Intake Map"),
    ],
)
_ENGINE_RPM = ParameterGroup(
    key="engine_rpm",
    name="Engine RPM",
    parameters=[
        priority(40160),
        low_level(40163),
        high_level(40162),
        event_only(40164),
        operand(40161),
        send_sms_to(7044),
        sms_text(8044, default_value="Engine RPM"),
    ],
)
_VEHICLE_SPEED = ParameterGroup(
    key="vehicle_speed",
    name="Vehicle speed",
    parameters=[
        priority(40170),
        low_level(40173),
        high_level(40172),
        event_only(40174),
        operand(40171),
        send_sms_to(7045),
        sms_text(8045, default_value="Vehicle speed"),
    ],
)
_TIMING_ADVANCE = ParameterGroup(
    key="timing_advance",
    name="Timing advance",
    parameters=[
        priority(40180),
        low_level(40183),
        high_level(40182),
        event_only(40184),
        operand(40181),
        send_sms_to(7046),
        sms_text(8046, default_value="Timing advance"),
    ],
)
_INTAKE_AIR_TEMPERATURE = ParameterGroup(
    key="intake_air_temperature",
    name="Intake air temperature",
    parameters=[
        priority(40190),
        low_level(40193),
        high_level(40192),
        event_only(40194),
        operand(40191),
        send_sms_to(7047),
        sms_text(8047, default_value="Intake air temperature"),
    ],
)
_MAF = ParameterGroup(
    key="maf",
    name="MAF",
    parameters=[
        priority(40200),
        low_level(40203),
        high_level(40202),
        event_only(40204),
        operand(40201),
        send_sms_to(7048),
        sms_text(8048, default_value="MAF"),
    ],
)
_THROTTLE_POSITION = ParameterGroup(
    key="throttle_position",
    name="Throttle position",
    parameters=[
        priority(40210),
        low_level(40213),
        high_level(40212),
        event_only(40214),
        operand(40211),
        send_sms_to(7049),
        sms_text(8049, default_value="Throttle position"),
    ],
)
_RUN_TIME_SINCE_ENGINE_START = ParameterGroup(
    key="run_time_since_engine_start",
    name="Run time since engine start",
    parameters=[
        priority(40220),
        low_level(40223),
        high_level(40222),
        event_only(40224),
        operand(40221),
        send_sms_to(7050),
        sms_text(8050, default_value="Run time since engine start"),
    ],
)
_DISTANCE_TRAVELED_MIL_ON = ParameterGroup(
    key="distance_traveled_mil_on",
    name="Distance traveled MIL on",
    parameters=[
        priority(40230),
        low_level(40233),
        high_level(40232),
        event_only(40234),
        operand(40231),
        send_sms_to(7051),
        sms_text(8051, default_value="Distance traveled MIL on"),
    ],
)
_RELATIVE_FUEL_RAIL_PRESSURE = ParameterGroup(
    key="relative_fuel_rail_pressure",
    name="Relative fuel rail pressure",
    parameters=[
        priority(40240),
        low_level(40243),
        high_level(40242),
        event_only(40244),
        operand(40241),
        send_sms_to(7052),
        sms_text(8052, default_value="Relative fuel rail pressure"),
    ],
)
_DIRECT_FUEL_RAIL_PRESSURE = ParameterGroup(
    key="direct_fuel_rail_pressure",
    name="Direct fuel rail pressure",
    parameters=[
        priority(40250),
        low_level(40253),
        high_level(40252),
        event_only(40254),
        operand(40251),
        send_sms_to(7053),
        sms_text(8053, default_value="Direct fuel rail pressure"),
    ],
)
_COMMANDED_EGR = ParameterGroup(
    key="commanded_egr",
    name="Commanded EGR",
    parameters=[
        priority(40260),
        low_level(40263),
        high_level(40262),
        event_only(40264),
        operand(40261),
        send_sms_to(7054),
        sms_text(8054, default_value="Commanded EGR"),
    ],
)
_EGR_ERROR = ParameterGroup(
    key="egr_error",
    name="EGR error",
    parameters=[
        priority(40270),
        low_level(40273),
        high_level(40272),
        event_only(40274),
        operand(40271),
        send_sms_to(7055),
        sms_text(8055, default_value="EGR error"),
    ],
)
_FUEL_LEVEL = ParameterGroup(
    key="fuel_level",
    name="Fuel level",
    parameters=[
        priority(40280),
        low_level(40283),
        high_level(40282),
        event_only(40284),
        operand(40281),
        send_sms_to(7056),
        sms_text(8056, default_value="Fuel level"),
    ],
)
_DISTANCE_TRAVELED_SINCE_CODES_CLEAR = ParameterGroup(
    key="distance_traveled_since_codes_clear",
    name="Distance traveled since codes clear",
    parameters=[
        priority(40290),
        low_level(40293),
        high_level(40292),
        event_only(40294),
        operand(40291),
        send_sms_to(7057),
        sms_text(8057, default_value="Distance traveled since codes clear"),
    ],
)
_BAROMETRIC_PRESSURE = ParameterGroup(
    key="barometric_pressure",
    name="Barometric pressure",
    parameters=[
        priority(40300),
        low_level(40303),
        high_level(40302),
        event_only(40304),
        operand(40301),
        send_sms_to(7058),
        sms_text(8058, default_value="Barometric pressure"),
    ],
)
_CONTROL_MODULE_VOLTAGE = ParameterGroup(
    key="control_module_voltage",
    name="Control module voltage",
    parameters=[
        priority(40310),
        low_level(40313),
        high_level(40312),
        event_only(40314),
        operand(40311),
        send_sms_to(7059),
        sms_text(8059, default_value="Control module voltage"),
    ],
)
_ABSOLUTE_LOAD_VALUE = ParameterGroup(
    key="absolute_load_value",
    name="Absolute load value",
    parameters=[
        priority(40320),
        low_level(40323),
        high_level(40322),
        event_only(40324),
        operand(40321),
        send_sms_to(7060),
        sms_text(8060, default_value="Absolute load value"),
    ],
)
_AMBIENT_AIR_TEMPERATURE = ParameterGroup(
    key="ambient_air_temperature",
    name="Ambient air temperature",
    parameters=[
        priority(40330),
        low_level(40333),
        high_level(40332),
        event_only(40334),
        operand(40331),
        send_sms_to(7061),
        sms_text(8061, default_value="Ambient air temperature"),
    ],
)
_TIME_RUN_WITH_MIL_ON = ParameterGroup(
    key="time_run_with_mil_on",
    name="Time run with MIL on",
    parameters=[
        priority(40340),
        low_level(40343),
        high_level(40342),
        event_only(40344),
        operand(40341),
        send_sms_to(7062),
        sms_text(8062, default_value="Time run with MIL on"),
    ],
)
_TIME_SINCE_TROUBLE_CODES_CLEARED = ParameterGroup(
    key="time_since_trouble_codes_cleared",
    name="Time since trouble codes cleared",
    parameters=[
        priority(40350),
        low_level(40353),
        high_level(40352),
        event_only(40354),
        operand(40351),
        send_sms_to(7063),
        sms_text(8063, default_value="Time since trouble codes cleared"),
    ],
)
_FUEL_TYPE = ParameterGroup(
    key="fuel_type",
    name="Fuel Type",
    parameters=[
        priority(40560),
        low_level(40563),
        high_level(40562),
        event_only(40564),
        operand(40561),
        send_sms_to(7633),
        sms_text(8633, default_value="Fuel Type"),
    ],
)
_ABSOLUTE_FUEL_RAIL_PRESSURE = ParameterGroup(
    key="absolute_fuel_rail_pressure",
    name="Absolute fuel rail pressure",
    parameters=[
        priority(40360),
        low_level(40363),
        high_level(40362),
        event_only(40364),
        operand(40361),
        send_sms_to(7064),
        sms_text(8064, default_value="Absolute fuel rail pressure"),
    ],
)
_HYBRID_BATTERY_PACK_REMAINING_LIFE = ParameterGroup(
    key="hybrid_battery_pack_remaining_life",
    name="Hybrid battery pack remaining life",
    parameters=[
        priority(40370),
        low_level(40373),
        high_level(40372),
        event_only(40374),
        operand(40371),
        send_sms_to(7065),
        sms_text(8065, default_value="Hybrid battery pack remaining life"),
    ],
)
_ENGINE_OIL_TEMPERATURE = ParameterGroup(
    key="engine_oil_temperature",
    name="Engine oil temperature",
    parameters=[
        priority(40380),
        low_level(40383),
        high_level(40382),
        event_only(40384),
        operand(40381),
        send_sms_to(7066),
        sms_text(8066, default_value="Engine oil temperature"),
    ],
)
_FUEL_INJECTION_TIMING = ParameterGroup(
    key="fuel_injection_timing",
    name="Fuel injection timing",
    parameters=[
        priority(40390),
        low_level(40393),
        high_level(40392),
        event_only(40394),
        operand(40391),
        send_sms_to(7067),
        sms_text(8067, default_value="Fuel injection timing"),
    ],
)
_FUEL_RATE = ParameterGroup(
    key="fuel_rate",
    name="Fuel Rate",
    parameters=[
        priority(40400),
        low_level(40403),
        high_level(40402),
        event_only(40404),
        operand(40401),
        send_sms_to(7068),
        sms_text(8068, default_value="Fuel Rate"),
    ],
)
_COMMAND_EQUIVALENCE_RATIO = ParameterGroup(
    key="command_equivalence_ratio",
    name="Command Equivalence Ratio",
    parameters=[
        priority(40460),
        low_level(40463),
        high_level(40462),
        event_only(40464),
        operand(40461),
        send_sms_to(7524),
        sms_text(8524, default_value="Command Equivalence Ratio"),
    ],
)
_INTAKE_MAP_2_BYTES = ParameterGroup(
    key="intake_map_2_bytes",
    name="Intake MAP (2 Bytes)",
    parameters=[
        priority(40470),
        low_level(40473),
        high_level(40472),
        event_only(40474),
        operand(40471),
        send_sms_to(7525),
        sms_text(8525, default_value="Intake MAP (2 Bytes)"),
    ],
)
_HYBRID_VEHICLE_SYSTEM_VOLTAGE = ParameterGroup(
    key="hybrid_vehicle_system_voltage",
    name="Hybrid Vehicle System Voltage",
    parameters=[
        priority(40480),
        low_level(40483),
        high_level(40482),
        event_only(40484),
        operand(40481),
        send_sms_to(7526),
        sms_text(8526, default_value="Hybrid Vehicle System Voltage"),
    ],
)
_HYBRID_VEHICLE_SYSTEM_CURRENT = ParameterGroup(
    key="hybrid_vehicle_system_current",
    name="Hybrid Vehicle System Current",
    parameters=[
        priority(40490),
        low_level(40493),
        high_level(40492),
        event_only(40494),
        operand(40491),
        send_sms_to(7527),
        sms_text(8527, default_value="Hybrid Vehicle System Current"),
    ],
)
_FAULT_CODES = ParameterGroup(
    key="fault_codes",
    name="Fault Codes",
    parameters=[
        priority(40420),
        event_only(40424),
        operand(40421),
        send_sms_to(7264),
        sms_text(8264, default_value="Fault Codes"),
    ],
)
_VIN = ParameterGroup(
    key="vin",
    name="VIN",
    parameters=[
        priority(40410),
        event_only(40414),
        operand(40411),
        send_sms_to(7241),
        sms_text(8241, default_value="VIN"),
    ],
)
_OEM_TOTAL_MILEAGE = ParameterGroup(
    key="oem_total_mileage",
    name="OEM Total Mileage",
    parameters=[
        priority(40430),
        low_level(40433),
        high_level(40432),
        event_only(40434),
        operand(40431),
        send_sms_to(7522),
        sms_text(8522, default_value="OEM Total Mileage"),
    ],
)
_OEM_FUEL_LEVEL = ParameterGroup(
    key="oem_fuel_level",
    name="OEM Fuel Level",
    parameters=[
        priority(40440),
        low_level(40443),
        high_level(40442),
        event_only(40444),
        operand(40441),
        send_sms_to(7529),
        sms_text(8529, default_value="OEM Fuel Level"),
    ],
)
_OEM_REMAINING_DISTANCE = ParameterGroup(
    key="oem_remaining_distance",
    name="OEM Remaining Distance",
    parameters=[
        priority(40520),
        low_level(40523),
        high_level(40522),
        event_only(40524),
        operand(40521),
        send_sms_to(7628),
        sms_text(8628, default_value="OEM Remaining Distance"),
    ],
)
_OEM_DISTANCE_UNTIL_SERVICE = ParameterGroup(
    key="oem_distance_until_service",
    name="OEM Distance Until Service",
    parameters=[
        priority(40510),
        low_level(40513),
        high_level(40512),
        event_only(40514),
        operand(40511),
    ],
)
_OEM_BATTERY_CHARGE_STATE = ParameterGroup(
    key="oem_battery_charge_state",
    name="OEM Battery Charge State",
    parameters=[
        priority(40570),
        low_level(40573),
        high_level(40572),
        event_only(40574),
        operand(40571),
        send_sms_to(7634),
        sms_text(8634, default_value="OEM Battery Charge State"),
    ],
)
_OEM_BATTERY_CHARGE_LEVEL = ParameterGroup(
    key="oem_battery_charge_level",
    name="OEM Battery Charge Level",
    parameters=[
        priority(40580),
        low_level(40583),
        high_level(40582),
        event_only(40584),
        operand(40581),
        send_sms_to(7635),
        sms_text(8635, default_value="OEM Battery Charge Level"),
    ],
)


OBD = ParameterGroup(
    key="obd",
    name="OBD II (Bluetooth)",
    groups=[
        _NUMBER_OF_DTC,
        _ENGINE_LOAD,
        _COOLANT_TEMPERATURE,
        _SHORT_FUEL_TRIM,
        _FUEL_PRESSURE,
        _INTAKE_MAP,
        _ENGINE_RPM,
        _VEHICLE_SPEED,
        _TIMING_ADVANCE,
        _INTAKE_AIR_TEMPERATURE,
        _MAF,
        _THROTTLE_POSITION,
        _RUN_TIME_SINCE_ENGINE_START,
        _DISTANCE_TRAVELED_MIL_ON,
        _RELATIVE_FUEL_RAIL_PRESSURE,
        _DIRECT_FUEL_RAIL_PRESSURE,
        _COMMANDED_EGR,
        _EGR_ERROR,
        _FUEL_LEVEL,
        _DISTANCE_TRAVELED_SINCE_CODES_CLEAR,
        _BAROMETRIC_PRESSURE,
        _CONTROL_MODULE_VOLTAGE,
        _ABSOLUTE_LOAD_VALUE,
        _AMBIENT_AIR_TEMPERATURE,
        _TIME_RUN_WITH_MIL_ON,
        _TIME_SINCE_TROUBLE_CODES_CLEARED,
        _FUEL_TYPE,
        _ABSOLUTE_FUEL_RAIL_PRESSURE,
        _HYBRID_BATTERY_PACK_REMAINING_LIFE,
        _ENGINE_OIL_TEMPERATURE,
        _FUEL_INJECTION_TIMING,
        _FUEL_RATE,
        _COMMAND_EQUIVALENCE_RATIO,
        _INTAKE_MAP_2_BYTES,
        _HYBRID_VEHICLE_SYSTEM_VOLTAGE,
        _HYBRID_VEHICLE_SYSTEM_CURRENT,
        _FAULT_CODES,
        _VIN,
        _OEM_TOTAL_MILEAGE,
        _OEM_FUEL_LEVEL,
        _OEM_REMAINING_DISTANCE,
        _OEM_DISTANCE_UNTIL_SERVICE,
        _OEM_BATTERY_CHARGE_STATE,
        _OEM_BATTERY_CHARGE_LEVEL,
    ],
)
