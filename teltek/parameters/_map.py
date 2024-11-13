from typing import Any

import teltek.parameters._db as db
from teltek.parameters._parameter import Parameter, ParameterGroup, ParameterIdRange


def map_raw_parameters(raw: dict[int, str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for group in db.ALL_GROUPS:
        group_out = _map_group(group, raw)
        if group_out:
            out[group.key] = group_out
    return out


def _map_group(group: ParameterGroup, raw: dict[int, str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for subgroup in group.groups:
        subgroup_out = _map_group(subgroup, raw)
        if subgroup_out:
            out[subgroup.key] = subgroup_out
    for parameter in group.parameters:
        value = _map_parameter(parameter, raw)
        if value is not None:
            out[parameter.key] = value
    return out


def _map_parameter(param: Parameter, raw: dict[int, str]) -> Any:
    if isinstance(param.id, ParameterIdRange):
        values: list[Any] = []
        for id in param.id.to_range():
            value = raw.get(id)
            if value is not None:
                value = param.convert_from_raw(value)
            values.append(value)
        # strip trailing None values
        while values and values[-1] is None:
            values.pop()
        if not values:
            return None
        return values
    else:
        value = raw.get(param.id)
        if value is not None:
            value = param.convert_from_raw(value)
        return value
