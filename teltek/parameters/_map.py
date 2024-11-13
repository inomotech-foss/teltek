from typing import Any, cast

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


def map_parameters_to_raw(values: dict[str, Any]) -> dict[int, str]:
    out: dict[int, str] = {}
    for group in db.ALL_GROUPS:
        group_values = values.get(group.key)
        if group_values is None:
            continue
        _map_group_to_raw(group, group_values, out=out)
    return out


def _map_group_to_raw(
    group: ParameterGroup, values: dict[str, Any], out: dict[int, str]
) -> None:
    for subgroup in group.groups:
        subgroup_values = values.get(subgroup.key)
        if subgroup_values is None:
            continue
        _map_group_to_raw(subgroup, subgroup_values, out=out)
    for parameter in group.parameters:
        _map_parameter_to_raw(parameter, values, out=out)


def _map_parameter_to_raw(
    param: Parameter,
    values: dict[str, Any],
    out: dict[int, str],
) -> None:
    if not isinstance(param.id, ParameterIdRange):
        try:
            value = values[param.key]
        except KeyError:
            return
        out[param.id] = param.convert_to_raw(value)
        return

    try:
        list_values = values[param.key]
    except KeyError:
        return
    assert isinstance(list_values, list)
    list_values = cast(list[Any], list_values)
    for idx, id in enumerate(param.id.to_range()):
        if idx < len(list_values):
            value = list_values[idx]
        else:
            value = None
        out[id] = param.convert_to_raw(value)
