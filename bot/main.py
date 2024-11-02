from parse_input import parse_input
from handlers_func import (
    add_contact, 
    change_contact, 
    show_phone, 
    show_all_contacts, 
    add_birthday, 
    show_birthday, 
    show_upcoming_birthdays
)
from address_book import AddressBook

def main():
    book = AddressBook()
    """Manages the main command processing cycle"""
    print(f"Welcome to the assistant bot!")
    while True:
        user_input = (
            input(
                """1. hello
2. add
3. change
4. phone
5. all
6.add-birthday
7.show-birthday
8.show-upcoming-birthday
9. exit or close
Enter a command: """
            )
            .strip()
        )
        parse_res = parse_input(user_input)
        cmd, *args = parse_res
        match cmd.lower():
            case "hello":
                print(f"How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all_contacts(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "show-upcoming-birthday":
                print(show_upcoming_birthdays(book))
            case "exit" | "close":
                print(f"Good bye!")
                break
            case _:
                print(f"Invalid command.\n")


if __name__ == "__main__":
    main()
