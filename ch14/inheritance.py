class StrKeyDict(dict):
    def __init__(self, iterable=None, **kwds):
        super().__init__()
        self.update(iterable, **kwds)

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    def __setitem__(self, key, item):
        super().__setitem__(str(key), item)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError: 
            return default

    def update(self, iterable=None, **kwds):
        if iterable is not None:
            try:
                pairs = iterable.items()
            except AttributeError: 
                pairs = iterable
            for key, value in pairs:
                self[key] = value

        if kwds:
            self.update(kwds)
