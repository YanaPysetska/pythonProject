# 1. Дано натуральне число N. Виведіть слово YES,
# якщо число N є точним ступенем двійки, або слово
# NO інакше. 8 - YES, 3 - NO
def func(n):
    while n >= 2:
        n = n / 2
    if 1 == n:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    n=int(input(f'Введите значение->'))
    func(n)
