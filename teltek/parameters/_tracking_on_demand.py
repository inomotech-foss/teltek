from teltek.parameters._parameter import (
    Parameter,
    ParameterGroup,
    ParameterType,
    ValueRange,
)

TRACKING_ON_DEMAND = ParameterGroup(
    key="tracking_on_demand",
    name="Tracking on Demand",
    parameters=[
        Parameter(
            key="period",
            id=10990,
            type=ParameterType.U8,
            default_value=10,
            value_range=ValueRange(5, 60),
            name="Tracking period",
        ),
        Parameter(
            key="duration",
            id=10991,
            type=ParameterType.U16,
            default_value=600,
            value_range=ValueRange(300, 3600),
            name="Tracking duration",
        ),
    ],
)
