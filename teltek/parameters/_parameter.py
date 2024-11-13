import dataclasses
import enum
from collections.abc import Iterator
from typing import Any, Self


@dataclasses.dataclass(frozen=True)
class ParameterIdRange:
    start: int
    end: int
    """inclusive"""

    def __len__(self) -> int:
        return self.end - self.start + 1

    def to_range(self) -> range:
        return range(self.start, self.end + 1)


class ParameterType(enum.StrEnum):
    U8 = "Uint8"
    U16 = "Uint16"
    U32 = "Uint32"
    I32 = "Int32"
    DOUBLE = "Double"
    STRING = "String"

    def is_integer(self) -> bool:
        return self in {
            ParameterType.U8,
            ParameterType.U16,
            ParameterType.U32,
            ParameterType.I32,
        }

    def is_numeric(self) -> bool:
        return self.is_integer() or self == ParameterType.DOUBLE

    def convert_from_raw(self, raw: str) -> Any:
        if self == ParameterType.STRING:
            return raw
        if raw == "":
            return None
        match self:
            case (
                ParameterType.U8
                | ParameterType.U16
                | ParameterType.U32
                | ParameterType.I32
            ):
                f = float(raw)
                i = int(f)
                if i != f:
                    raise ValueError(f"Expected integer, got {f}")
                return i
            case ParameterType.DOUBLE:
                return float(raw)

    def convert_to_raw(self, value: Any) -> str:
        if value is None:
            return ""
        return str(value)


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

    def iter_parameter_ids(self) -> Iterator[int]:
        if isinstance(self.id, int):
            yield self.id
        else:
            yield from self.id.to_range()

    def map_value_to_key(self, value: int) -> str:
        if self.value_map is None:
            raise ValueError(f"No value map for {self.key}")
        for mapping in self.value_map:
            if mapping.value == value:
                return mapping.key
        raise ValueError(f"No mapping for value {value}")

    def map_key_to_value(self, key: str) -> int:
        if self.value_map is None:
            raise ValueError(f"No value map for {self.key}")
        for mapping in self.value_map:
            if mapping.key == key:
                return mapping.value
        raise ValueError(f"No mapping for key {key}")

    def convert_from_raw(self, raw: str) -> Any:
        value = self.type.convert_from_raw(raw)
        if value is None:
            return None
        if self.value_map is not None:
            return self.map_value_to_key(value)
        return value

    def convert_to_raw(self, value: Any) -> str:
        if self.value_map is not None:
            value = self.map_key_to_value(value)
        return self.type.convert_to_raw(value)


@dataclasses.dataclass(frozen=True, kw_only=True)
class ParameterGroup:
    key: str
    name: str
    groups: list[Self] = dataclasses.field(default_factory=list)
    parameters: list[Parameter] = dataclasses.field(default_factory=list)

    def iter_parameter_ids(self) -> Iterator[int]:
        for group in self.groups:
            yield from group.iter_parameter_ids()
        for parameter in self.parameters:
            yield from parameter.iter_parameter_ids()
