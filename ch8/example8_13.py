from collections.abc import Sequence


def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]


animals = "drake fawn heron ibex koala lynx tahr xerus yak zapus".split()
table = columnize(animals)
for row in table:
    print("".join(f"{word:10}" for word in row))
