import dataclasses
from typing import Any, Protocol, Self


class _FromDict(Protocol):
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self: ...


@dataclasses.dataclass(frozen=True)
class PaginatedData[T]:
    current_page: int
    from_item: int
    to_item: int
    total_items: int
    first_page: int
    last_page: int
    per_page: int
    data: list[T]

    @classmethod
    def from_dict[D: _FromDict](
        cls, item_cls: type[D], data: dict[str, Any]
    ) -> "PaginatedData[D]":
        return PaginatedData(
            current_page=int(data["current_page"]),
            from_item=int(data["from"]),
            to_item=int(data["to"]),
            total_items=int(data["total"]),
            first_page=int(data["first_page"]),
            last_page=int(data["last_page"]),
            per_page=int(data["per_page"]),
            data=[item_cls.from_dict(item) for item in data["data"]],
        )
