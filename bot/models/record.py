from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:
    # A class for storing information about a contact, including name and phone list.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


    def remove_phone(self, phone):
        self.phones.remove(Phone(phone))


    def edit_phone(self, old_phone, new_phone):
        if Phone(old_phone) not in self.phones:
            raise ValueError(f'Phone "{old_phone}" not found!') 
        else: 
            self.remove_phone(old_phone)
            self.add_phone(new_phone)


    def find_phone(self, phone:str) -> Phone:
        if Phone(phone) not in self.phones:
            raise ValueError(f'Phone "{phone}" not found!')
        return Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"