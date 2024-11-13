import dataclasses
import enum
from typing import Self


@dataclasses.dataclass(frozen=True)
class ParameterIdRange:
    start: int
    end: int
    """inclusive"""


class ParameterType(enum.StrEnum):
    U8 = "Uint8"
    U16 = "Uint16"
    U32 = "Uint32"
    I32 = "Int32"
    DOUBLE = "Double"
    STRING = "String"


@dataclasses.dataclass(frozen=True)
class ValueRange:
    min: float | int | str
    max: float | int | str


@dataclasses.dataclass(frozen=True)
class ValueMapping:
    key: str
    value: int
    display: str


@dataclasses.dataclass(frozen=True, kw_only=True)
class Parameter:
    key: str
    id: int | ParameterIdRange
    type: ParameterType
    default_value: float | int | str | None
    value_range: ValueRange
    """for string type, min and max are the length of the string"""
    name: str
    value_map: list[ValueMapping] | None = None


@dataclasses.dataclass(frozen=True, kw_only=True)
class ParameterGroup:
    key: str
    name: str
    groups: list[Self] = dataclasses.field(default_factory=list)
    parameters: list[Parameter] = dataclasses.field(default_factory=list)
