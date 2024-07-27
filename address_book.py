# from collections import UserDict

# class Field:
#     # Field: Базовий клас для полів запису.
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     # Name: Клас для зберігання імені контакту. Обов'язкове поле
#     pass

# class Phone(Field):
#     # Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
#         phone = Field
#         def _validate_phone(self, phone):
#         # Перевірка, що номер телефону складається з 10 цифр
#             return phone.isdigit() and len(phone) == 10

# # ﻿Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр)

# class Record:
#     # Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []
    

#     def add_phone(self):
#            self.phones.append(Phone)
    

#     def remove_phone(self):
#            self.phones.pop(self.name)
    

#     def edit_phone(self):
#            self.name = Field
    

#     def find_phone(self):
#            Field.__name__ = self.data

#     # реалізація класу

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     # AddressBook: Клас для зберігання та управління записами.

#     def add_record(self):
#            self.data = Record
    
    
#     def find(self):
#            Record.__name__ = self.data
    
    
#     def delete(self):
#            Record.__name__ = self.data.pop()
    
    
		


# # # Створення нової адресної книги. Dictioanry
# book = AddressBook()

# #     # Створення запису для John
# john_record = Record("John")
# print(john_record)

# # john_record.add_phone("5555555555")
# #print(john_record)

# #     # Додавання запису John до адресної книги
# #book.add_record(john_record)

# #     # Створення та додавання нового запису для Jane
# #     jane_record = Record("Jane")
# #     jane_record.add_phone("9876543210")
# #     book.add_record(jane_record)

# #     # Виведення всіх записів у книзі
# #     for name, record in book.data.items():
# #         print(record)

# #     # Знаходження та редагування телефону для John
# #     john = book.find("John")
# #     john.edit_phone("1234567890", "1112223333")

# #     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# #     # Пошук конкретного телефону у записі John
# #     found_phone = john.find_phone("5555555555")
# #     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# #     # Видалення запису Jane
# #     book.delete("Jane")


from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Name: Клас для зберігання імені контакту. Обов'язкове поле.
    pass

class Phone(Field):
    # Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        if self._validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must be exactly 10 digits.")

    def _validate_phone(self, phone):
        # Перевірка, що номер телефону складається з 10 цифр
        return phone.isdigit() and len(phone) == 10

class Record:
    # Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            self.add_phone(new_phone)

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # AddressBook: Клас для зберігання та управління записами.
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Приклад використання
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі після видалення
for name, record in book.data.items():
    print(record)
