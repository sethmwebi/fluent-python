from typing import Protocol, runtime_checkable
from example13_18 import RandomPicker

@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(self, Iterable) -> None: ...
