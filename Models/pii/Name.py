from dataclasses import dataclass

from helpers.StaticHelpers import list_eq
from models.PrimaryIndexedList import PrimaryIndexedList


@dataclass
class Name:
    prefixes: list[str]
    first: PrimaryIndexedList
    middle: PrimaryIndexedList
    last: PrimaryIndexedList
    suffixes: list[str]
    titles: list[str]
    preferred_name: str

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.first == other.first \
                and self.middle == other.middle \
                and self.last == other.last \
                and self.preferred_name == other.preferred_name \
                and list_eq(self.prefixes, other.prefixes) \
                and list_eq(self.suffixes, other.suffixes) \
                and list_eq(self.titles, other.titles)
        return False

    def __str__(self):
        return (
            f'{' '.join(self.prefixes) if self.prefixes else ''}'
            f'{' '.join(self.first.items) if self.first.items else ''}'
            f'{' '.join(self.middle.items) if self.middle.items else ''}'
            f'{' '.join(self.last.items) if self.last.items else ''}'
            f'{' '.join(self.suffixes) if self.suffixes else ''}'
            f'{' '.join(self.titles) if self.titles else ''}'
        )

    def __hash__(self):
        return hash(
            (
                tuple(self.prefixes),
                tuple(self.titles),
                tuple(self.suffixes),
                self.preferred_name,
                self.first.__hash__(),
                self.middle.__hash__(),
                self.last.__hash__()
            )
        )
