import dataclasses
import enum
from collections.abc import Iterator
from typing import Any, Self


@dataclasses.dataclass(frozen=True)
class ParameterIdRange:
    start: int
    end: int
    """inclusive"""

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

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
        if self == ParameterType.DOUBLE:
            # must match with max_raw_len
            return f"{value:.6f}"
        return str(value)

    def max_raw_len(self, max_value: int | float) -> int:
        match self:
            case (
                ParameterType.U8
                | ParameterType.U16
                | ParameterType.U32
                | ParameterType.I32
            ):
                return len(str(max_value))
            case ParameterType.DOUBLE:
                # teltonika seems to use 6 decimal places
                return len(f"{max_value:.6f}")
            case ParameterType.STRING:
                # the max_value is the max length of the string
                return int(max_value)


@dataclasses.dataclass(frozen=True)
class ValueRange:
    min: float | int
    max: float | int


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
    value_is_bitflag: bool = False
    value_map: list[ValueMapping] | None = None

    def iter_ids(self) -> Iterator[int]:
        if isinstance(self.id, int):
            yield self.id
        else:
            yield from self.id.to_range()

    def _debug_id(self) -> str:
        return f"{self.key} ({self.id})"

    def map_value_to_key(self, value: int, *, retain: bool = False) -> str:
        if self.value_map is None:
            raise ValueError(f"No value map in {self._debug_id()}")
        if self.value_is_bitflag:
            keys: list[str] = []
            for mapping in self.value_map:
                if mapping.value & value:
                    keys.append(mapping.key)
            if keys:
                return "|".join(keys)

        for mapping in self.value_map:
            if mapping.value == value:
                return mapping.key
        if retain:
            return str(value)
        raise ValueError(f"No mapping for value {value} in {self._debug_id()}")

    def map_key_to_value(self, key: str) -> int:
        if self.value_map is None:
            raise ValueError(f"No value map in {self._debug_id()}")
        value = 0
        parts = key.split("|") if self.value_is_bitflag else [key]
        for part in parts:
            found = False
            for mapping in self.value_map:
                if mapping.key == part:
                    value += mapping.value
                    found = True
                    break
            if found:
                continue
            if part.isdigit():
                value += int(part)
                continue
            raise ValueError(f"No mapping for key {part} in {self._debug_id()}")
        return value

    def convert_from_raw(self, raw: str, *, lenient: bool = False) -> Any:
        try:
            value = self.type.convert_from_raw(raw)
        except Exception as exc:
            raise ValueError(
                f"Failed to convert {raw} to {self.type} in {self._debug_id()}"
            ) from exc
        if value is None:
            return None
        if self.value_map is not None:
            return self.map_value_to_key(value, retain=lenient)
        return value

    def convert_to_raw(self, value: Any) -> str:
        if self.value_map is not None:
            try:
                value = self.map_key_to_value(value)
            except Exception as exc:
                raise ValueError(
                    f"Failed to convert {value} to {self.type} in {self._debug_id()}"
                ) from exc
        return self.type.convert_to_raw(value)

    def max_raw_len(self) -> int:
        return self.type.max_raw_len(self.value_range.max)


@dataclasses.dataclass(frozen=True, kw_only=True)
class ParameterGroup:
    key: str
    name: str
    groups: list[Self] = dataclasses.field(default_factory=list)
    parameters: list[Parameter] = dataclasses.field(default_factory=list)

    def iter_parameters(self) -> Iterator[Parameter]:
        for group in self.groups:
            yield from group.iter_parameters()
        yield from self.parameters

    def iter_parameter_ids(self) -> Iterator[int]:
        for parameter in self.iter_parameters():
            yield from parameter.iter_ids()
