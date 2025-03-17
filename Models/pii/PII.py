from dataclasses import dataclass

from Name import Name
from models.pii.Email import Email
from models.pii.SSN import SSN
from models.pii.address.Address import Address
from models.pii.phone.PhoneNumber import PhoneNumber


@dataclass
class PII:
    name: Name
    ssn: SSN
    phone_number: PhoneNumber
    email: Email
    address: Address

    def __eq__(self, other):
        if isinstance(other, PII):
            return self.name == other.name \
                and self.ssn == other.ssn \
                and self.phone_number == other.phone_number \
                and self.email == other.email \
                and self.address == other.address
        return False

    def __hash__(self):
        return hash((
            self.name.__hash__(),
            self.ssn.__hash__(),
            self.phone_number.__hash__(),
            self.email.__hash__(),
            self.address.__hash__(),
        ))
