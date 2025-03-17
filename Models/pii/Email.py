from dataclasses import dataclass


@dataclass
class Email:
    local_part: str
    domain: str

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.domain == other.domain and self.local_part == other.local_part
        return False

    def __str__(self):
        return f'{self.local_part}@{self.domain}'

    def __hash__(self):
        return hash((self.local_part, self.domain))

