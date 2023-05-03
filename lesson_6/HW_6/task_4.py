# 4.Напишіть функцію change_list, яка приймає
# список і змінює місця його перший і останній
# елемент. У вихідному списку щонайменше 2 елементи.
def change_list(x):
    if len(x) > 1:
        x[0], x[-1] = x[-1], x[0]
    return print("Измененный список:", x)
if __name__ == '__main__':
    x=list(map(int, input('Введите числа->').split()))
    change_list(x)