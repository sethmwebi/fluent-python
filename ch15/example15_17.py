import random

from collections.abc import Iterable
from typing import TypeVar, Generic

from ch13.example13_7 import Tombola

T = TypeVar('T')

class LottoBlower(Tombola, Generic[T]):
    def __init__(self, items: Iterable[T]) -> None:
        self._balls = list[T](items)

    def load(self, iterable: Iterable[T]) -> None:
        self._balls.extend(iterable)

    def pick(self) -> T:
        try:
            position = random.randrange(len(self._balls))
        except ValueError: 
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:
        return tuple(self._balls)
