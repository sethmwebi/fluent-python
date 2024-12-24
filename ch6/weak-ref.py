import weakref


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Cheese({self.kind!r})"


stock = weakref.WeakValueDictionary()
catalog = [
    Cheese("Red Leicester"),
    Cheese("Tilsit"),
    Cheese("Brie"),
    Cheese("Parmesan"),
]

for cheese in catalog:
    stock[cheese.kind] = cheese


# print(sorted(stock.keys()))
# del catalog
# print(sorted(stock.keys()))
# del cheese
class MyList(list):
    """list subclasses whose instances may be weakly referenced"""


a_list = MyList(range(10))

# a_list can be the target of a weak reference
wref_to_a_list = weakref.ref(a_list)
print(wref_to_a_list)
