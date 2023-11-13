from abc import ABC, abstractmethod
from collections import UserDict
from datetime import datetime, timedelta
import pickle

class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone(value)

    def validate_phone(self, phone):
        if not (len(phone) == 10 and phone.isdigit()):
            raise ValueError("Invalid phone number format")

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_birthday(value)

    def validate_birthday(self, birthday):
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid birthday format (should be 'YYYY-MM-DD')")

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None


    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        initial_length = len(self.phones)
        self.phones = [p for p in self.phones if p.value != phone]
        if len(self.phones) == initial_length:
            raise ValueError("Phone number not found")

    def edit_phone(self, old_phone, new_phone):
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                new_phone_instance = Phone(new_phone)
                try:
                    new_phone_instance.validate_phone(new_phone_instance.value)
                except ValueError as e:
                    print(e)
                    return
                phone_obj.value = new_phone
                return
        print("Phone number not found")
    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now()
            if isinstance(self.birthday, Birthday):
                next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
                if today > next_birthday:
                    next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
                days_left = (next_birthday - today).days
                return days_left
            else:
                return None
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, N=1):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i + N]

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
                for name, record_data in data.items():
                    record = Record(record_data['name'], record_data['phone'])
                    if 'birthday' in record_data:
                        record.birthday = Birthday(record_data['birthday'])
                    self.add_record(record)
        except FileNotFoundError:
            pass

    def search(self, query):
        results = []
        for record in self.data.values():
            if query in record.name.value:
                results.append(record)
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
        return results

class UserInterface(ABC):
    @abstractmethod
    def add_record(self, name, phone, birthday):
        pass

    @abstractmethod
    def find_record(self, name):
        pass

    @abstractmethod
    def delete_record(self, name):
        pass

    @abstractmethod
    def list_records(self):
        pass

    @abstractmethod
    def edit_phone(self, name, old_phone, new_phone):
        pass

    @abstractmethod
    def add_phone(self, name, phone):
        pass

    @abstractmethod
    def remove_phone(self, name, phone):
        pass

    @abstractmethod
    def days_to_birthday(self, name):
        pass

class ConsoleUserInterface(UserInterface):
    def __init__(self, address_book):
        self.address_book = address_book

    def add_record(self, name, phone, birthday):
        record = Record(name, phone, birthday)
        self.address_book.add_record(record)
        print("Record added.")

    def find_record(self, name):
        record = self.address_book.find(name)
        if record:
            print(record)
        else:
            print("Record not found.")

    def delete_record(self, name):
        self.address_book.delete(name)
        print("Record deleted.")

    def list_records(self):
        for record in self.address_book.data.values():
            print(record)

    def edit_phone(self, name, old_phone, new_phone):
        record = self.address_book.find(name)
        if record:
            try:
                record.edit_phone(old_phone, new_phone)
                print("Phone number edited.")
            except ValueError as e:
                print(e)
        else:
            print("Record not found.")

    def add_phone(self, name, phone):
        record = self.address_book.find(name)
        if record:
            try:
                record.add_phone(phone)
                print("Phone number added.")
            except ValueError as e:
                print(e)
        else:
            print("Record not found.")

    def remove_phone(self, name, phone):
        record = self.address_book.find(name)
        if record:
            try:
                record.remove_phone(phone)
                print("Phone number removed.")
            except ValueError as e:
                print(e)
        else:
            print("Record not found.")

    def days_to_birthday(self):
        name = input("Enter name to check days to birthday: ")
        record = self.address_book.find(name)
        if record:
            days_left = record.days_to_birthday()
            if days_left is not None:
                print(f"Days until {name}'s birthday: {days_left}")
            else:
                print(f"{name} has no birthday date set.")
        else:
            print("Record not found.")

if __name__ == "__main__":
    address_book = AddressBook()
    console_interface = ConsoleUserInterface(address_book)

    while True:
        print("\nMenu:")
        print("1. Add Record")
        print("2. Find Record")
        print("3. Delete Record")
        print("4. Edit Phone Number")
        print("5. Add Phone Number")
        print("6. Remove Phone Number")
        print("7. Days to Birthday")
        print("8. List Records")
        print("9. Quit")

        choice = input("Enter your choice:")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            birthday = input("Enter birthday (optional): ")
            if birthday:
                record = Record(name, phone, birthday)
            else:
                record = Record(name, phone)
            console_interface.add_record(record)
        elif choice == "2":
            name = input("Enter name to find: ")
            console_interface.find_record(name)
        elif choice == "3":
            name = input("Enter name to delete: ")
            console_interface.delete_record(name)
        elif choice == "4":
            name = input("Enter name to edit phone number: ")
            old_phone = input("Enter the old phone number: ")
            new_phone = input("Enter the new phone number: ")
            console_interface.edit_phone(name, old_phone, new_phone)
        elif choice == "5":
            name = input("Enter name to add phone number: ")
            phone = input("Enter the phone number to add: ")
            console_interface.add_phone(name, phone)
        elif choice == "6":
            name = input("Enter name to remove phone number: ")
            phone = input("Enter the phone number to remove: ")
            console_interface.remove_phone(name, phone)
        elif choice == "7":
            console_interface.days_to_birthday()
        elif choice == "8":
            console_interface.list_records()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select a valid option.")