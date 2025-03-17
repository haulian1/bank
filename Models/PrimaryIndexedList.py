from dataclasses import dataclass

from helpers.StaticHelpers import list_eq
from models.errors_and_exceptions.InvalidInitializationError import InvalidInitializationError


@dataclass
class PrimaryIndexedList:
    primary: set[int]
    items: list[any]

    def __post_init__(self):
        out_of_bounds_indexes: list[str] = []
        for index in self.primary:
            if index >= len(self.items):
                out_of_bounds_indexes.append(str(index))

        if len(out_of_bounds_indexes) > 0:
            raise InvalidInitializationError(f'Primary index(es): {','.join(out_of_bounds_indexes)} '
                                             f'cannot be greater than the length of the list of items.')

    def __eq__(self, other):
        if isinstance(other, PrimaryIndexedList):
            return self.primary == other.primary \
                and list_eq(self.items, other.items)
        return False

    def __str__(self):
        return ", ".join(self.items)

    def __hash__(self):
        return hash((tuple(self.primary), tuple(self.items)))
