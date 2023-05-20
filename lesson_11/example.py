# class Student:
#     def __init__(self, name,  grade):
#         self.name = name
#         self.grade = grade
#     def success_review(self):
#         if self.grade>=60:
#             print(f'{self.name}, Успішний студент')
#         else:
#             print(f'{self.name}, НЕ успішний студент')
#
# student=Student('Анна',60)
# student.success_review()

# class Calculator:
#     def __init__(self):
#         pass
#     def add(self,first_number,second_number):
#         return first_number+second_number
#
#     def subtract(self,first_number,second_number):
#         return first_number-second_number
#
#     def multiply(self,first_number,second_number):
#         return first_number*second_number
#
#     def divide(self,first_number,second_number):
#         return first_number/second_number
#
# calculator = Calculator()
#
# result1 = calculator.add(5, 3)
# print(result1)  # Виведе 8
#
# result2 = calculator.subtract(10, 4)
# print(result2)  # Виведе 6
#
# result3 = calculator.multiply(2, 6)
# print(result3)  # Виведе 12
#
# result4 = calculator.divide(15, 3)
# print(result4)  # Виведе 5.0

# class Car:
#     def __init__(self, mileage):
#         self.__mileage =mileage
#
#     def drive(self, distance):
#         self.__mileage+=distance
#
#     def get_mileage(self):
#         return self.__mileage
#
# new_car=Car(1000)
#
# new_car.drive(200)
# new_car.drive(300)
#
# print(new_car.get_mileage())

# class BankAccount:
#     def __init__(self,  owner, balance):
#         self.owner=owner
#         self.balance=balance
#
#     def deposit(self, amount):
#         self.balance+=amount
#
#     def withdraw(self, amount):
#         if self.balance<amount:
#             print("повідомлення про помилку")
#         else:
#             self.balance-=amount
#     def get_balance(self):
#         return self.balance
#
#     def owner_info(self):
#         print('Ovner',self.owner )
#         print('Balance', self.balance)
#
# obj_new=BankAccount('Joe', 1000)
#
# obj_new.deposit(200)
#
# obj_new.withdraw(800)
#
# obj_new.owner_info()

# class Person:
#     def __init__(self, name, age):
#         self.__name=name
#         self.__age=age
#
#     def display_info(self):
#         print(f'Имя {self.__name}')
#         print(f'Возраст {self.__age} ')
#
#     def set_age(self, age):
#         self.__age=age
#
# person=Person('Yana', 29)
#
# person.set_age(30)
#
# person.display_info()

# class Car:
#     def __init__(self, brand, color):
#         self.brand=brand
#         self.color=color
#     def start_engine(self):
#         print("Запуск двигателя")
#     def drive(self):
#          print("Поехали!")
#
# car=Car('Audi', 'red')
# car.start_engine()
# car.drive()

from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        super().calculate_area()
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, side_a):
        self.side_a=side_a
    def calculate_area(self):
        super().calculate_area()
        return self.side_a*self.side_a

circle=Circle(10)
rectangle=Rectangle(5)

calculate_circle=circle.calculate_area()
calculate_rectangle=rectangle.calculate_area()

print(f'Площадь круга {calculate_circle}')
print(f'Площадь квадрата {calculate_rectangle}')