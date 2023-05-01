# Entity representing a student
from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass
class Student:
    """Class representing a student"""

    firstname: str
    lastname: str
    birthdate: date
    balance: int
    gpa: Optional[float] = None
    id: Optional[int] = None