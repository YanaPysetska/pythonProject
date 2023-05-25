# #2. Написать класс для сущности Точка(содержит в себе координаты Х и Y)
# # Написать классы для сущностей Треугольник, Квадрат,
# # которые аггрегируют объекты класса Точка.
# # Написать методы, которые считают площадь фигур,
# # если координаты введены правильно. Если нет, то показать
# # сообщение об ошибке.
import math
class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
class Triangle:
    def __init__(self,points, x2, y2, x3, y3):
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.points = points
    def calculate_triangle_area(self):
        triangle_area= abs(self.points.x * (self.y2 - self.y3) + self.x2 * (self.y3 - self.points.y) + self.x3 * (self.points.y - self.y2)) / 2.0
        return triangle_area
class Square:
    def __init__(self,points, x2, y2):
        self.points = points
        self.x2 = x2
        self.y2 = y2
    def calculate_square_area(self):
        side_length = abs(self.x2 - self.points.x)
        square_area = side_length * side_length
        return square_area

try:
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    points = Point(x, y)


    area = Triangle(points, 2, 4, 3, 2)
    calculate_triangle=area.calculate_triangle_area()

    area_2=Square(points, 5, 5)
    calculate_square=area_2.calculate_square_area()

    print(f'Площадь треугольника {calculate_triangle}')
    print(f'Площадь квадрата {calculate_square}')

except ValueError:
    print("Ошибка, введите число")
