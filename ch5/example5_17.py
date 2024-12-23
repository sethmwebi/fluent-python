from dataclasses import dataclass
from typing import ClassVar

from example5_15 import ClubMember


@dataclass
class HackerClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handles.add(self.handle)
