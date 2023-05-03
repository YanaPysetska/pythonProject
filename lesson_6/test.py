#Финкция создать

#это тело функции с параметрами в дужках
# def get_max_number(a, b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(get_max_number(11, 12)) #вызов функции присвоили значения
#
# max_value=get_max_number(110, 12) #аргументы в дужках
# print(max_value)


#параметры по умолчанию
# def get_max_number(a, b=10):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(get_max_number(7, 6))

#ключевые параметры и tuple
# def get_max_number(a, b=10):
#     if a>b:
#         return a, True
#     else:
#         return b, False
#
# value=get_max_number(2,4)
# print(type(value))
# print(value)
#
# value, is_true=value
# print(value, is_true)


#позиционные аргументы
#*args  - tuple
#**kwargs - dict
# def get_max_number(age,type, *numbers, lesson=1, **addition_params):
#     max_number=numbers[0]
#     for number in numbers:
#         if number>max_number:
#             max_number=number
#     if addition_params.get('lesson')==5:
#         print(addition_params['my_name'])
#     print(age)
#     print(type)
#     return max_number
#
# print(get_max_number(1, int, 5, 22 ,23, my_name='Vadim', book='Python')) #ключевые элементы со значением

#локальные и глобальные переменные
# x=50 # глобальная переменная вне функции, внутри функции может измениться
# def func(x):
#     print(f'x={x}')
#     x=2
#     print(f'We change x to {x}')
# func(x)
# print(f'Finish x={x}')

# x=50
# def func():
#     global x
#     print(f'x={x}')
#     x=2
#     print(f'We change x to {x}')
#
# func()
# print(f'Finish x={x}')

#типизация
# def get_max_number(a:int, b:int) -> int:
#     if a>b:
#         return float(a)
#     else:
#         return b
# print(get_max_number(1,2))
# print(get_max_number(2.3,2))

#функция которая получает x как аргумент -> и отдает x*x
def func(x):
    return x*x
# print(func(5))
# #lambda - ключевое слово, после нее аргумент
# f=lambda x:x*x
# print(f)
# print(f(5))
# #lambda - ключевое слово, после нее аргументы x,y
# sum_func=lambda x,y:x+y
# print(sum_func(3,5))
#функция в функции
# def func(x):
#     def func_1(x):
#         print(f'Our x is {x}')
#     func_1(x)
#     return x*x

#map and filter

#map(func, *iterables)
# my_list1=[2, 10, 10]
# my_list2=[3,20]
# def sum_two_number(x,y):
#     return x+y
# result=list(map(sum_two_number, my_list1, my_list2))
# result_2=list(map(lambda x,y:x*y, my_list1, my_list2))
# print(result)
# print(result_2)

#filter
# my_list1=[2, 10, 10,67]
# my_list2=[3,20]
# result=list(filter(lambda x:x>50, my_list1))
# print(result)

from import_1 import print_hi
import import_1
print_hi()