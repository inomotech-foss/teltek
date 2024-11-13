from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterIdRange,
    ParameterType,
    ValueRange,
)

_PARAMETERS: list[Parameter] = [
    Parameter(
        key="sim_roaming_operator_list",
        id=ParameterIdRange(5000, 5049),
        type=ParameterType.U32,
        default_value=0,
        value_range=ValueRange(0, 999999),
        name="SIM roaming operator list",
    ),
    Parameter(
        key="operator_blacklist",
        id=ParameterIdRange(5500, 5549),
        type=ParameterType.U32,
        default_value=0,
        value_range=ValueRange(0, 999999),
        name="Operator blacklist",
    ),
]

GSM = ParameterGroup(
    key="gsm",
    name="GSM",
    parameters=_PARAMETERS,
)
