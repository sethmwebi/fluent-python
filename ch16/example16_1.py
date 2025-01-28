from collections import abc
from array import array
import reprlib
import math
import functools
import operator
import itertools

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented

    def __index__(self):
        if len(self) == 0:
            raise ValueError("Cannot convert an empty Vector to an integer index")
        return int(round(abs(self)))
    def __len__(self):
        return len(self._components)

    def __lt__(self, other):
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        elif isinstance(other, (int, float)):
            return abs(self) < other
        return NotImplemented

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError: 
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError: 
            return NotImplemented
        return Vector(n * factor for n in self)

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        if(isinstance(other, abc.Sized) and isinstance(other, abc.Iterable)):
            if len(self) == len(other):
                return sum(a *b for a, b in zip(self, other))
            else:
                raise ValueError('@ requires vectors of equal length.')
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other
    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    __match_args__ = ('x', 'y', 'z', 't')

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError: 
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if(n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode) # type: ignore
        return cls(memv)
