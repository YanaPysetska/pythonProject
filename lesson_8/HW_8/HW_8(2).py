import re

class Record:
    def __init__(self, name, phone):
        self.__name = self.__pattern_validate_name(name)
        self.__phone = self.__pattern_validate_phone(phone)

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone

    def __pattern_validate_name(self, name):
        pattern_name = r'^[A-Za-zА-Яа-я]+$'
        if re.match(pattern_name, name):
            return name
        else:
            raise ValueError("Некорректное имя")

    def __pattern_validate_phone(self, phone):
        pattern_phone = r'^\+\d{11}$'
        if re.match(pattern_phone, phone):
            return phone
        else:
            raise ValueError("Некорректный телефон")


class Directory:
    def __init__(self):
        self.records = []

    def add_record(self, name, phone):
        try:
            record = Record(name, phone)
            self.records.append(record)
            print("Запись успешно добавлена.")
        except ValueError as e:
            print(str(e))

    def remove_record_by_name(self, name):
        for record in self.records:
            if record.get_name() == name:
                self.records.remove(record)
                print("Запись удалена.")
                return
        print("Запись с указанным именем не найдена.")

    def edit_subscriber(self):
        name = input("Введите имя абонента для редактирования: ")
        for record in self.records:
            if record.get_name() == name:
                print("Введите новые данные:")
                new_name = input("Введите новое имя: ")
                new_phone = input("Введите новый номер телефона: ")
                try:
                    record._Record__name = record._Record__pattern_validate_name(new_name)
                    record._Record__phone = record._Record__pattern_validate_phone(new_phone)
                    print("Данные абонента успешно обновлены.")
                    return
                except ValueError as e:
                    print(str(e))
        print("Абонент с указанным именем не найден.")

    def get_all_records(self):
        return self.records
class Interface:
    def __init__(self):
        self.directory = Directory()
    def run(self):
        while True:
            print("1. Добавить запись")
            print("2. Удалить запись")
            print("3. Редактировать запись")
            print("4. Выйти")

            choice = input("Выберите действие (1-4): ")

            if choice == "1":
                name = input("Введите имя: ")
                phone = input("Введите телефон который начинается с символа "+" и содержит 11 цифр: ")
                self.directory.add_record(name, phone)
            elif choice == "2":
                name = input("Введите имя записи для удаления: ")
                self.directory.remove_record_by_name(name)
            elif choice == "3":
                self.directory.edit_subscriber()
            elif choice == "4":
                print("Программа завершена.")
                break
            else:
                print("Некорректный выбор.")

            records = self.directory.get_all_records()
            print("Текущий список записей:")
            for record in records:
                print(f"Имя: {record.get_name()}, Телефон: {record.get_phone_number()}")

if __name__ == "__main__":
    interface = Interface()
    interface.run()
