#структурировать функции
#есть соц сети

# user={
#     'name':'John',
#     'surname':'Snow'
# }
# print(f'{user["name"]} {"surname"}')


#чтобы не дублировать код нужны классы. его нужно описать
class PhoneNumber:
    def __init__(self, number):
        self.number=number

    def format_to_ukr(self):
        return f'+38{self.number}'


class User:
    #функция в классе - МЕТОД
#    prefix = 'Sir'#переменная класа
    def __init__(self, name, surname,number): #сюда лучше всего заносить все переменные
        prefix='Sir'
        a = 1#можно писать и такие переменные которые мы нигде использовать не будем
        self.name = name
        self.phone_number=PhoneNumber(number)
        self.surname = surname
        self.sir_name = prefix+name

# self - передаем, когда пишем функцию
#self - когда используют методы или переменные
    def get_whole_name(self):
        return f'{self.name } {self.surname}'
    @staticmethod
    def new_method():
        return 1+1
#метод без   self нужен чтобы сделать что-то внутри функции
#удалить лишние пробелы в сообщении
#удаляем лишние пробелы
    @staticmethod
    def strip(msg:str):
        return msg.strip()

    def mod_name(self):
        name=self.get_whole_name()
        name='Sir' + name
        self.sir_name=name
    def show_all(self):
        full_name =self.get_whole_name()
        phone = self.phone_number.format_to_ukr()
        return f'My name is:{full_name}. \nMy phone number is:{phone}'
#Два класса которые наследуються
class Developer(User):
    def __init__(self, name, surname,number, position):
        #передаем то что с родительского класса
        super().__init__(name, surname,number)
        self.position=position
    def do_some_bug_in_code(self):
        print('Working on new bug')

    def show_all(self):
        full_name = self.get_whole_name()
        return f"Name: {full_name}. i'm{self.position}"

class QA(User):
    def do_some_bug(self):
        print('Find some bug')



# dev1=Developer('Jonny', 'Mnemonic', 123456789)
# dev1.do_some_bug_in_code()
# print(dir(dev1))
#
# print(dev1.phone_number.number)

# user_1=User('John', 'Snow',123456789)
# print(user_1.show_all())
#
# user_2=User('John','Dow')
#
# print(user_1.get_whole_name())
# print(user_2.get_whole_name())
#
# user_1.new_method()
# print(user_1.strip('My message'))
#
#
# print(user_1.sir_name)
# user_1.mod_name()
# print(user_1.sir_name)
#
# user_1.new_method()
dev1=Developer('Jonny', 'Mnemonic', 123456789, 'Senior Developer')
print(dev1.show_all())
#Полиморфиз (многоликий) работает с разными типами данных

