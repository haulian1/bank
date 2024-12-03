from dataclasses import dataclass

from Enums import CardinalDirections


@dataclass
class Address:
    house_number: int
    cardinal_direction: CardinalDirections
    street_name: str
    unit_designation: str
    city: str
    state: str
    postal_code:str
    country: str

    def one_line(self):
        return self.__str__().replace('\n', ', ')

    def __str__(self):
        return (f'{self.house_number}'
                f'{' ' if self.cardinal_direction is None else f' {self.cardinal_direction.name} '}'
                f'{self.street_name}'
                f'{'' if self.unit_designation is None else f'\n{self.unit_designation}'}'
                f'\n{self.city}, '
                f'{self.state} '
                f'{self.postal_code}'
                f'\n{self.country}')
