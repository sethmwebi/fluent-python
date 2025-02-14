from dataclasses import InitVar, dataclass
from typing import Optional


@dataclass
class C:
    i: int
    j: Optional[int] = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup("j")


c = C(10, database=my_database)
