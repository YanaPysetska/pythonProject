# 5. Напишіть функцію to_dict(lst), яка приймає аргумент
# у вигляді списку і повертає словник, в якому кожен елемент
# списку є ключем і значенням. Передбачається, що елементи
# списку відповідатимуть правилам завдання ключів у словниках.
def to_dict(lst):
# правилам завдання ключів - убираем повторяющиеся значения
    unique_lst = list(set(lst))
    result = {}
    for i in range(len(unique_lst)):
        result.update({unique_lst[i]: unique_lst[i]})
    return print(result)
if __name__ == '__main__':
    lst=list(input('Введите значение листа->').split())
    to_dict(lst)