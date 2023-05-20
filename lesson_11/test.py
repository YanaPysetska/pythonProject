#ООП
#наследование

# class Person:
#     brain=True
#     def __init__(self, first_name, last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def get_name(self):
#         return f'My name {self.first_name}'
#
# property=Person('Joe', 'Coen')
# print(property.first_name)
# print(property.get_name())
# print(property.brain)
#
# class Student(Person):
#     def __init__(self, first_name, last_name, graduate):
#         super().__init__(first_name, last_name)
#         self.graduate=graduate
#
#     def get_graduate(self):
#         return f'My graduate {self.graduate}'
#
#     def get_name(self):
#         return f'My name {self.first_name} in student class'
#
# student=Student('Marta', 'Lee', 'Master')
#
# print(student.get_graduate())
# print(student.get_name())

#Инкапсуляция
# class Student:
#     def __init__(self, first_name, last_name, graduate):
#         self.first_name=first_name #public
#         self._last_name = last_name #protected
#         self.__graduate = graduate #private
#
#     def get_graduate(self):
#         return self.__graduate
#
#     def _get_first_name(self):
#         return self.first_name
#     def __get_last_name(self):
#         return self._last_name
#
# student=Student('Joe', 'Coin', 'Master')
# print(student.first_name)
# print(student._last_name)
# print(student._Student__graduate)
# #посмотреть как методызаписаны
# print(student.__dict__)
#
# print(student.get_graduate())
# print(student._get_first_name())
# print(student._Student__get_last_name())

#Полиморфизм
print(len('My string'))
print(len([1,2,3,4]))
print(len({'Name':'Joe', 'Address':'Kyiv'}))

