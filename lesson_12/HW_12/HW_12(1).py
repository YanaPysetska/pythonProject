# Використовуючи модуль argparse створити програму
# розрахунку квадратного рівняння.
# (Реалізацію самого рівняння можете взяти з минулих ДЗ)
# Запуск програми python main.py -a={} -b={} c={}
# де параметри (a, b, c - параметри квадратного рівняння),
# за замовчуванням параметр а = 0
# При виклику програми з прапорцем --help
# вивести інформацію про програму та про параметри.

import math
import argparse
import sys

parser=argparse.ArgumentParser(description="Программа розрахунку квадратного рівняння")
parser.add_argument('-a', type=float, default=0, help='значення_a')
parser.add_argument('-b', type=float, help='значення_b')
parser.add_argument('-c', type=float, help='значення_c')
args=parser.parse_args()
def quadratic_equation(a,b,c):
    try:
        discr = b ** 2 - 4 * a * c

        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return x1, x2
        elif discr == 0:
            x = -b / (2 * a)
            return x
        else:
            return None
    except ZeroDivisionError:
        print('Измените значение а')

if __name__ == "__main__":
    print (quadratic_equation(args.a, args.b, args.c))

