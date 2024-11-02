from collections import UserDict
from models.record import Record
from models.birthday import Birthday
from datetime import datetime, timedelta

class AddressBook(UserDict):
    # A class for storing and managing addresses.
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def search_record(self, name: str) -> Record:
        return self.data[name]

    def delete_by_name(self, name):
        del self.data[name] 

    def get_upcoming_birthdays(self) -> list:
        # This function returns users whose birthdays fall 7 days ahead of the current day
        today = datetime.now().date()
        date_after7 = today + timedelta(days=7)

        congrats_list = []

        for user in self.data.values():
            birthday_date = datetime.strptime(user.birthday.value, '%d.%m.%Y').date()
            birthday_date = birthday_date.replace(year=today.year)
            if today <= birthday_date <= date_after7:
                if birthday_date.weekday() == 5:
                    birthday_date += timedelta(days=2)
                elif birthday_date.weekday() == 6:
                    birthday_date += timedelta(days=1)
                format_date = datetime.strftime(birthday_date, '%d.%m.%Y')
                congrats_list.append({"name": user.name.value, "congrats_date": format_date})

        return congrats_list
