# 2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0
# (користувач вводить a, b, c), якщо дискримінант
# від'ємний викликати виняток DiscriminantError
# і вивести відповідне повідомлення.

import math
a=int(input('Value 1-> '))
b=int(input('Value 2-> '))
c=int(input('Value 3-> '))
disc = b*b-(4 * a * c)
print(f"дискриминант D -> {disc}")
try:
    root = math.sqrt(disc)
    print(f"Квадратный корень -> {root}")
except ValueError:
    print('DiscriminantError')
else:
    if disc==0:
        x_zero_D= -b / 2*a
        print(f'уравнение имеет только один корень {x_zero_D}')
    else:
        x_1 = (-+root) / (2 * a)
        x_2 = (-b-root) / (2 * a)
        print(f'Два различных вещественных корня: {x_1} и {x_2}')

#вариант 2
class DiscriminantError(Exception):
    pass
import math
a=int(input('Value 1-> '))
b=int(input('Value 2-> '))
c=int(input('Value 3-> '))
disc = b*b-(4 * a * c)
print(f"дискриминант D -> {disc}")
if disc<0:
    raise DiscriminantError
    root = math.sqrt(disc)
    print(f"Квадратный корень -> {root}")
else:
    if disc==0:
        x_zero_D= -b / 2*a
        print(f'уравнение имеет только один корень {x_zero_D}')
    else:
        x_1 = (-+root) / (2 * a)
        x_2 = (-b-root) / (2 * a)
        print(f'Два различных вещественных корня: {x_1} и {x_2}')

# 3. Напишіть інтерактивний калькулятор. Передбачається, що користувач
# вводить формулу, що складається з числа, оператора (як мінімум + і -)
# та іншого числа, розділених пробілом (наприклад, 1 + 1).
# Використовуйте str.split()
# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн
# FormulaError.
# b. Спробуйте перетворити перший і третій елемент на float
# ( float_value = float(str_value)). Спіймайте будь-яку ValueError
# і згенеруйте замість нього FormulaError
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError

class FormulaError(Exception):
    def __init__(self, message="Некоректна формула"):
        self.message = message
        super().__init__(self.message)
while True:
    formula=input('Input number, operator and another number ->')
    try:
        list_formula=formula.split( )
        print(list_formula)
        if len(list_formula)!=3:
            raise FormulaError
        float_value_num_1 = float(list_formula[0])
        float_value_num_2 = float(list_formula[2])
    except FormulaError as fe:
        print('exception_1',fe.message)
    except ValueError:
        print('ЖОПА')
    else:
        try:
            arifmetic_command=list_formula[1]
            if arifmetic_command=='+':
                result_plus=float_value_num_1 + float_value_num_2
                print(result_plus)
            elif arifmetic_command=='-':
                result_minus=float_value_num_1 - float_value_num_2
                print(result_minus)
            else:
                raise FormulaError("Некоректна формула")
        except FormulaError as fe:
            print('exception_3', fe.message)
        break
#вариант 2
class FormulaError(Exception):
    pass
while True:
    formula=input('Input number, operator and another number ->')
    try:
        list_formula=formula.split( )
        print(list_formula)
        if len(list_formula)!=3:
            raise FormulaError
        float_value_num_1 = float(list_formula[0])
        float_value_num_2 = float(list_formula[2])
    except FormulaError:
        raise FormulaError
    except ValueError:
        raise FormulaError
    else:
        try:
            arifmetic_command=list_formula[1]
            if arifmetic_command=='+':
                result_plus=float_value_num_1 + float_value_num_2
                print(result_plus)
            elif arifmetic_command=='-':
                result_minus=float_value_num_1 - float_value_num_2
                print(result_minus)
            else:
                raise FormulaError
        except FormulaError:
            raise FormulaError
        break