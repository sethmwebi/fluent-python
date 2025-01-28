import random
from example13_7 import Tombola

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    
    def load(self, iterable): 
        self._items.extend(iterable if isinstance(iterable, list) else list(iterable))
        self._randomizer.shuffle(self._items)


    def pick(self):
        try:
            return self._items.pop()
        except IndexError: 
            raise LookupError('pick from empty BingoCage') 

    def __call__(self):
        self.pick()

class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError: 
                msg = ('right operand in += must be "Tombola" or an iterable')
                raise TypeError(msg)
        self.load(other_iterable)
        return self
