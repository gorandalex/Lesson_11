from collections import UserDict
from datetime import datetime



class AdressBook(UserDict):
    N = 10
    current_index = 0

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self):
        names = sorted([name for name in self.data])
        while AdressBook.current_index < len(self.data):
            text_records = ''
            for name in names[AdressBook.current_index:min(len(self.data), AdressBook.current_index + AdressBook.N)]:
                record = self.data[name]
                record_name = record.name.value
                record_birthday = str(record.birthday) 
                for phone in record.phones:
                    text_records += '{:<20}{:>20}{:>20}\n'.format(record_name, phone.value, record_birthday)
                    record_name = ''
                    record_birthday = ''
                if record_name:
                    text_records += '{:<20}{:>20}{:>20}\n'.format(record_name, '', record_birthday)

            yield text_records
            AdressBook.current_index += AdressBook.N
            


class Record():
    def __init__(self, name, phone = None, birthday = None):
        self.name = Name(name)

        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = ''

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def delete_phone(self, phone):
        phone_obj = Phone(phone)    
        if phone_obj in self.phones:
            self.phone.remove(phone_obj)

    def change_phone(self, old_phone, new_phone):
        phone_obj = Phone(old_phone)    
        if phone_obj in self.phones:
            self.phones[self.phones.index(phone_obj)] = Phone(new_phone)

    def days_to_birthday(self):
        date_now = datetime.now()
        try:
            date_birthday = datetime(year=date_now.year, month=self.month, day=self.day)
        except:
             date_birthday = datetime(year=date_now.year, month=self.month, day=self.day - 1)

        if date_birthday < date_now:
            try:
                date_birthday = datetime(year=date_now.year + 1, month=self.month, day=self.day)
            except:
                date_birthday = datetime(year=date_now.year + 1, month=self.month, day=self.day - 1)

        return (date_birthday - date_now).days
           



class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value:str):
        if not all((value.startswith('+'), len(value) == 13, value[1:].isdigit())):
            raise ValueError("Введіть номер в форматі '+380111111111'")
        self.__value = value

class Birthday(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return datetime.strftime(self.__value, '%d.%m.%Y')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            date_birthday = datetime.strptime(value, '%d.%m.%Y')
            self.__value = date_birthday
        except:
            raise ValueError("Введіть день народження в форматі 'дд.мм.ггг' (наприклад 01.01.1990)")
            
            

