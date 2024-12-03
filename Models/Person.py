import uuid
from dataclasses import dataclass
from datetime import date

from Address import Address


@dataclass
class Person:
    first_name: str
    last_name: str
    middle_name: str
    date_of_birth: date
    address: Address
    person_id: uuid = uuid.uuid4()

    def __post_init__(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        if self.middle_name:
            self.middle_name = self.middle_name.upper()

    def full_name(self,
                  first_initial=False,
                  middle_initial=False,
                  last_initial=False,
                  include_middle=False):
        first = self.first_name[0] if first_initial else self.first_name
        middle = (f' {self.middle_name[0]} ' if middle_initial else f' {self.middle_name} ') if include_middle else ' '
        last = self.last_name[0] if last_initial else self.last_name
        return f'{first}{middle}{last}'

    def __str__(self):
        return (f'{self.first_name}'
                f'{' ' if self.middle_name is None else f' {self.middle_name} '}'
                f'{self.last_name}'
                f'\n{self.date_of_birth}'
                f'\n{self.address}'
                f'\n{self.person_id}')
