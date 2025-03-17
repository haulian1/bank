from dataclasses import dataclass

from helpers.StaticHelpers import *


@dataclass
class Address:
    address_lines: dict[int, (str, str)]

    def __hash__(self):
        return dict_int_tuple_str_str_hash(self.address_lines)

    def __eq__(self, other):
        if isinstance(other, Address):
            return dict_int_tuple_str_str_equals(self.address_lines, other.address_lines)
        return False

    def __str__(self):
        return dict_int_tuple_str_str_str(self.address_lines, values_only=True, preserve_insertion_order=False)


a = {}
b = {}

a[1] = ("hi", "hello")
a[2] = ("wow", "wee")

b[2] = ("wow", "wee")
b[1] = ("hi", "hello")

z = Address(a)
x = Address(b)

print()
print(z)
print(x)
print(z == x)

b[3] = ("yo", "no")

print()
print(z)
print(x)
print(z == x)

c = {}
c[z] = "z"
c[x] = "x"

print(c)

