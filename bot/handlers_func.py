from prettytable import PrettyTable
from models.name import Name
from models.record import Record
from address_book import AddressBook
from models.birthday import Birthday


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    """User adding"""
    if len(args) < 2:
        raise ValueError("Give me name and phone please")
    name, phone_number = args
    if name in book:
        record = book.search_record(name)
    else:
        record = Record(name)
    record.add_phone(phone_number)
    book.add_record(record)
    return f"Contact added."

@input_error
def change_contact(args, book: AddressBook):
    """Changing the phone number by user name"""
    if len(args) < 3:
        raise ValueError("Give me name, old and new phone please")
    name, old_phone_number, new_phone_number = args
    record = book.search_record(name)
    record.edit_phone(old_phone_number, new_phone_number)
    return f"Contact updated."

@input_error
def show_phone(args, book: AddressBook):
    """Display user phone number by name"""
    if len(args) < 1:
        raise ValueError("Give me name please")
    name = args[0]
    if name in book:
        phone_number = book[name]
        return f"Your phone number is: {phone_number}"
    else:
        return f"User not found"

@input_error
def show_all_contacts(book: AddressBook):
    '''Display information about all users'''
    table = PrettyTable()
    table.field_names = ["Name", "Phone Numbers"]
    for _, record in book.items():
        table.add_row([record.name.value, str.join('\n', [phone.value for phone in record.phones])])
    print(f"All users information:\n{table}")


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Give me your name and birthday date please")
    name, birthday = args
    record = book.search_record(name)
    record.add_birthday(birthday)
    return f"Birthday added"

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Give me name please")
    name = args[0]
    record = book.search_record(name)
    return f"{record.name.value} birthday is {record.birthday.value}"

@input_error
def show_upcoming_birthdays(book: AddressBook):
    '''Display upcoming birthdays'''
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays"
    return str.join('\n', [f"{record['name']} birthday is on {record['congrats_date']}" for record in upcoming])
