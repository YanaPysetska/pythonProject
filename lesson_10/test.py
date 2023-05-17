#any()-> [] принимает лист
#all()-> []

# a=[1,2]
# b=4
# c='hi'
# d=2
#
# #if a==2 or b==2 or c==2 or d==2 запистаь такой пример с any
#
# if all([a,b,c,d]):
#     print("True")
# else:
#     print("False")
#
# #генератор
# print(any([True for i in range(10000) if i==5000]))

#pip install pyyaml -
#pip list - посмотреть пакеты


#decorators
#функция
# def cat():
#     print('Meo')
#
# cat()
# #функция в функции
# def cat():
#     def say():
#         return 'Meo'
#     return say()
#
# print(cat())


#функция вызывает функцию
# def say_something():
#     return 'Glory Ukraine'
#
# def say_after_func(func):
#     print(func)
#     print('Do something')
#
# say_after_func(say_something())

# def animal(type_animal='cat'):
#     def cat():
#         return 'Meo'
#
#     def dog():
#         return 'Woow'
#
#     if type_animal == 'cat':
#         return cat
#     else:
#         return dog
#
# print(animal())

# def my_decorator(func):
#     def my_wrapper():
#         print(f'Start')
#         func()
#         print(f'End')
#     return my_wrapper()
#
# @my_decorator
# def dog():
#     print('Woow !')
#
# dog()

#декоратор который принимает некоторые элементы

# def my_decorator(func):
#     def my_wrapper(arg1, arg2):
#         print(f'I get {arg1} and {arg2}')
#         func(arg1, arg2)
#     return my_wrapper
#
# def full_name(first_name, last_name):
#     print(f'My full name {first_name} {last_name}' )
#
# full_name('joe', 'Koen')

#передаем не вызначену кол-во аргументов

# def my_decorator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f'I get args - {args}')
#         print(f'I get kwargs - {kwargs}')
#         func(*args, **kwargs)
#     return my_wrapper
#
# @my_decorator
# def my_func(*args, **kwargs):
#     for _ in args:
#         print(_)
#     print(f'Our kwargs {kwargs}')
#     print('hi')
#
# my_func(1,22,3, 4, q=2, p=4)
# my_func()

#не знает какое кол-во элементов будет получать
# def summ(*args):
#     print(args)
#     print(sum((args)))
#
# summ(1, 2, 3, 4, 33, 43, 23)

# def summ(*args, c=12, d=22):
#
#     print(args)
#     print(sum((args)))
# summ(1, 2, 3, 4, 33, 43, 23)

#КЛАССЫ

# john={
#     'name':'Joe',
#     'age':23,
#     'salary':2000
# }
#
# Mark={
#     'name':'Mark',
#     'age':25,
#     'salary':22000
# }
#
# def get_name(person:dict)->str:
#     return person['name']
#
# def update_salsry(person:dict)->str:
#     return person['salary']*0.1

# LOCAL_VAR='Python'
# class People:
#     country='Ukraine'
# #функция внутри класса это метод
#
#     def __init__(self, name:str, age:int):
#         self.name=name
#         self.age=age
#
#     def my_name_is(self) ->str:
#         return f'my name {self.name}'
#
#     def my_age(self) ->str:
#         return f'my age {self.age}'
#
#     def language(self) ->str:
#         return f'my language {LOCAL_VAR}'
#
# vadym: People=People('Vadym', 20)
#
# print(vadym.my_name_is())
# print(vadym.language())

#класс без конструктора
import random
from random import randint
class DataGeneration:
    def generation_name(name):
        new_name=f'{name} {randint(1, 50000)}'
        return new_name

data_generator=DataGeneration
print(data_generator.generation_name('Joe'))

print(DataGeneration.generation_name('Marta'))