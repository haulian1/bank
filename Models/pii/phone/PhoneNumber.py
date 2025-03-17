from dataclasses import dataclass

from helpers.StaticHelpers import *


@dataclass
class PhoneNumber:
    groups: dict[int, (str, str)]

    def __eq__(self, other):
        if isinstance(other, PhoneNumber):
            return dict_int_tuple_str_str_equals(self.groups, other.groups)
        return False

    def __hash__(self):
        return dict_int_tuple_str_str_hash(self.groups)

    def __str__(self):
        return dict_int_tuple_str_str_str(self.groups)
