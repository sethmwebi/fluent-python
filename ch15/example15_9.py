from example15_4 import BookDict
import json


def from_json(data: str) -> BookDict:
    whatever: BookDict = json.loads(data)
    return whatever
