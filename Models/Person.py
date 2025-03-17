import uuid
from dataclasses import dataclass

from models.pii.PII import PII


@dataclass
class Person:
    id: uuid
    personal_info: PII
