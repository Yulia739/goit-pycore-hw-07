import re
from models.field import Field

class Phone(Field):
    # Class for storing the phone number. It has a format validation (10 digits).
    def __init__(self, value):
        if self._validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("The phone number must contain 10 digits.")
        
    @staticmethod
    def _validate_phone(value):
        return bool(re.fullmatch(r"\d{10}", value))