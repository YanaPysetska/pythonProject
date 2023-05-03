# #Создане новых дерриторий:
# import os
# directory = os.getcwd()
# for i in range(1, 7):
#     filename = f"test_{i}.txt"
#     file_path = os.path.join(directory, filename)
#     with open(file_path, "w"):
#         pass

# 1. Дано натуральне число N. Виведіть слово YES,
# якщо число N є точним ступенем двійки, або слово
# NO інакше. 8 - YES, 3 - NO
from task_1 import func
if __name__ == '__main__':
    func(8)

# 2. Напишіть функцію square, яка приймає 1 аргумент, сторону
# квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.

from task_2 import square
if __name__ == '__main__':
    square(4)

#3. Напишіть функцію is_prime, яка приймає 1
# аргумент - число від 2 до 1000, і повертає
# True, якщо це просте число, і False в іншому випадку.
from task_3 import is_prime
if __name__ == '__main__':
    is_prime(3)

# 4.Напишіть функцію change_list, яка приймає
# список і змінює місця його перший і останній
# елемент. У вихідному списку щонайменше 2 елементи.
from task_4 import change_list
if __name__ == '__main__':
    change_list(list(map(int, input('Введите числа->').split())))

# 5. Напишіть функцію to_dict(lst), яка приймає аргумент
# у вигляді списку і повертає словник, в якому кожен елемент
# списку є ключем і значенням. Передбачається, що елементи
# списку відповідатимуть правилам завдання ключів у словниках.

from task_5 import to_dict
if __name__ == '__main__':
    to_dict(list(input('Введите значение листа->').split()))

# 6.Напишіть функцію sum_range(start, end),
# яка підсумовує всі цілі числа від значення
# start до величини end включно. Якщо користувач
# задасть перше число більше, ніж друге, просто
# поміняйте їх місцями
from task_6 import sum_range
if __name__ == '__main__':
    sum_range(2,5)
