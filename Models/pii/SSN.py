import re
from dataclasses import dataclass


def validate_SSN(ssn: str) -> bool:
    with_dashes = '[0-9]{3}-[0-9]{2}-[0-9]{4}'
    without_dashes = '[0-9]{9}'
    if re.match(with_dashes, ssn) or re.match(without_dashes, ssn):
        return True
    return False


@dataclass
class SSN:
    first: str
    middle: str
    last: str

    def __post_init__(self):
        validate_SSN(self.__str__())

    def __eq__(self, other):
        if isinstance(other, SSN):
            return self.__str__() == other.__str__()
        return False

    def __str__(self):
        return f'{self.first}-{self.middle}-{self.last}'

    def __hash__(self):
        return hash(self.__str__())
