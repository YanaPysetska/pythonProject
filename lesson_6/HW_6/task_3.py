# Напишіть функцію is_prime, яка приймає 1
# аргумент - число від 2 до 1000, і повертає
# True, якщо це просте число, і False в іншому випадку.
import sympy
def is_prime(n):
    while True:
        if n>=2 and n<=1000:
            if sympy.isprime(n) == True:
                print('це просте число')
            else:
                print('це Не просте число')
            break
        else:
            n = int(input(f'Введите значение от 2 до 10001->'))
if __name__ == '__main__':
    n = int(input(f'Введите значение->'))
    is_prime(n)