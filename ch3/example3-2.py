from collections import OrderedDict


def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


b1 = dict(api=1, author="Robert Green", type="book", title="48 Laws of Power")
# print(get_creators(b1))
b2 = OrderedDict(
    api=2, type="book", title="Why Nations Fail", authors="Darron Acemouglu".split()
)
# print(get_creators(b2))
# print(get_creators({"type": "book", "pages": 770}))
# get_creators("spam, spam, spam")
food = dict(category="ice cream", flavor="vanilla", cost=199)
match food:
    case {"category": "ice cream", **details}:
        print(f"Ice cream details: { details}")
