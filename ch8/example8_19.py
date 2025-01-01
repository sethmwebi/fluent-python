from typing import Iterable, TypeVar

T = TypeVar("T", bound="SupportsRichComparison")


class SupportsRichComparison:
    def __lt__(self, other: "SupportsRichComparison") -> bool: ...
    def __gt__(self, other: "SupportsRichComparison") -> bool: ...


def top(series: Iterable[T], length: int) -> list[T]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
