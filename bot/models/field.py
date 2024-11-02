class Field:
    # Base class for record fields.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Field):
            return False
        return self.value == other.value
    
    def __hash__(self) -> int:
        return self.value.__hash__()