import math
from typing import NamedTuple, SupportsAbs

class Vector2d(NamedTuple):
    x: float
    y: float

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

def is_unit(v: SupportsAbs[float]) -> bool:
    """'True' if the magnitude of 'v' is close to 1."""
    return math.isclose(abs(v), 1.0)
