# 6.Напишіть функцію sum_range(start, end),
# яка підсумовує всі цілі числа від значення
# start до величини end включно. Якщо користувач
# задасть перше число більше, ніж друге, просто
# поміняйте їх місцями
def sum_range(start, end):
    if start>end:
        start,end=end,start
    sum_numbers = 0
    for i in range(start, end + 1):
            sum_numbers += i
    return print(f'Результат -> {sum_numbers}')
if __name__ == '__main__':
    start=int(input('Введите 1 значение->'))
    end=int(input('Введите 2 значение->'))
    sum_range(start, end)


