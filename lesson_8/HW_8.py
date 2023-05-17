#1. Написать свой тип данных для сложения и вычитания, сравнение
# комплексных чисел. А так же правильного отображение их
# в консоли(magic method __str__).
import cmath
class Complex_numbers:
    def __init__(self, a, b, c, d):
        x=complex(a,b)
        print(x)
        y=complex(c,d)
        print(y)
        plus_com=x+y
        print(f'сложения {plus_com}')
        minus_com=x-y
        print(f'вычитания {minus_com}')

    def __str__(self):
        return f'{self.a}'
        return f'{self.b}'


result=Complex_numbers(1,2,3,4)
