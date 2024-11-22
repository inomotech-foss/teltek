import dataclasses
import gzip
from collections.abc import Iterable
from pathlib import Path
from typing import Any, BinaryIO, Self

from teltek.parameters._map import map_raw_parameters


@dataclasses.dataclass(frozen=True)
class Config:
    configuration_version: str
    hw_version: str
    title: str
    min_configurator_version: str
    fm_type: str
    spec_id: int

    raw_parameters: dict[int, str]

    @classmethod
    def _from_pairs(cls, pairs: Iterable[tuple[str, str]]) -> Self:
        kwargs: dict[str, Any] = {}
        raw_parameters: dict[int, str] = {}
        for key, value in pairs:
            match key:
                case "ConfigurationVersion":
                    kwargs["configuration_version"] = value
                case "HwVersion":
                    kwargs["hw_version"] = value
                case "Title":
                    kwargs["title"] = value
                case "MinConfiguratorVersion":
                    kwargs["min_configurator_version"] = value
                case "FmType":
                    kwargs["fm_type"] = value
                case "SpecId":
                    kwargs["spec_id"] = int(value)
                case _:
                    if not key.isdigit():
                        raise ValueError(f"Unknown non-parameter key: {key}")
                    param_id = int(key)
                    raw_parameters[param_id] = value

        return cls(**kwargs, raw_parameters=raw_parameters)

    def _to_pairs(self) -> Iterable[tuple[str, str]]:
        yield "ConfigurationVersion", self.configuration_version
        yield "HwVersion", self.hw_version
        yield "Title", self.title
        yield "MinConfiguratorVersion", self.min_configurator_version
        yield "FmType", self.fm_type
        yield "SpecId", str(self.spec_id)
        for param_id, value in self.raw_parameters.items():
            yield str(param_id), value

    @classmethod
    def _from_content(cls, content: str) -> Self:
        def pairs():
            for raw_pair in content.split(";"):
                if not raw_pair:
                    continue
                key, _, value = raw_pair.partition(":")
                yield (key, value)

        return cls._from_pairs(pairs())

    def to_content(self) -> str:
        return ";".join(f"{key}:{value}" for key, value in self._to_pairs())

    @classmethod
    def read(cls, path: Path | BinaryIO) -> Self:
        with gzip.open(path, "r") as f:
            content = f.read()
        return cls._from_content(content.decode())

    def write(self, path: Path | BinaryIO) -> None:
        content = self.to_content()
        with gzip.open(path, "w") as f:
            f.write(content.encode())

    def map_raw_parameters(self) -> dict[str, Any]:
        return map_raw_parameters(self.raw_parameters)
