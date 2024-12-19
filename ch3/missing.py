from collections import UserDict, abc


def _upper(x):
    try:
        return x.upper()
    except AttributeError:
        return x


class DictSub(dict):
    def __missing__(self, key):
        return self[_upper(key)]


class UserDictSub(UserDict):
    def __missing__(self, key):
        return self[_upper(key)]


class SimpleMappingSub(abc.Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    # next three methods: abstract in ABC
    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    # never called by instances of this class
    def __missing__(self, key):
        return self[_upper(key)]


class MappingMissingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]


class DictLikeMappingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __contains__(self, key):
        return key in self._data


# d = DictSub(A="letter A")
# print(d["a"])
# print(d.get("a", ""))
# print("a" in d)
# ud = UserDictSub(A="letter A")
# print(ud["a"])
# print(ud.get("a", ""))
# print("a" in ud)
# sms = SimpleMappingSub(A="letter A")
# print("a" in sms)
# mms = MappingMissingSub(A="letter A")
# print("a" in mms)
dms = DictLikeMappingSub(A="letter A")
print("a" in dms)
