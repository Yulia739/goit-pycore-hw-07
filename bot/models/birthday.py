from datetime import date, datetime
from models.field import Field
import re

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")