# #класс для хранения координат
# #простейшее определение класа. его нужно называть с большой буквы
# class Vector:
#     MIN_COORD=0
#     MAX_COORD=100
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <=arg <= cls.MAX_COORD
#     def __init__(self, x, y):
#         self.x=self.y=0
#         if Vector.validate(x) and Vector.validate(y):
#             self.x=x
#             self.y=y
#     def get_coord(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x*x+y*y
#
# v=Vector(1, 200)
# print(Vector.norm2(5, 6))



# #метод финализатор
#     def __del__(self):
#         print("Удаление экземпляра" + str(self))
# #метод:
#     def set_coords(self, x, y):
#         self.x=0
#         self.y=0
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
#
#
# pt=Point(1,2)
# print(pt.__dict__)

# pt=Point()
# pt2=Point()
# pt.set_coords(1,2)
# pt2.set_coords(10,20)
# print(pt.get_coords())
# print(pt2.get_coords())
# f=getattr(pt, 'get_coords')
# print(f())
#посмотреть все атрибуты класа:
#Point.__dict__

#Создание экземляра класа:
#b=Point() - имеют те же свойства
#посмотреть к чему пренадлежит экземпляр
#type(a)
#Point.circle=1 - меняем значение атрибута
#Получаем - что все для всех экземпляров поменялось это свойство
#a.color='green' - тут для отельного обьекта меняем значение свойства

#магический метод __new__
# class Point:
# #cls -обязателен
#
#     def __new__(cls, *args, **kwargs):
#         print("вызов __new__ для" + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0 ,y=0):
#         print("вызов __init__ для" + str(self))
#         self.x=x
#         self.y=y
#
# pt=Point(1,2)

import accessify
from accessify import private, protected
class Point:
    def __init__(self, x=0 ,y=0):
        self.__x=self.__y=0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Нужно число')

    def get_coord(self):
        return self.__x, self.__y

pt=Point(1,2)
pt.set_coord(10,20)
pt.check_value(5)
