from typing import Any, Protocol


class SupportsLessThan(Protocol):  # <1>
    def __lt__(self, other: Any) -> bool: ...  # <2>
