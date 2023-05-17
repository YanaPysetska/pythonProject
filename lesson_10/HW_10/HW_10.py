# Створити декоратор який кожен раз буде записувати у
# файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих
# аргументів *args). Запис в файл формату
# ""Function launched at {час запуску} with result
#     {результат роботи функції}
import datetime
def test_time(func):
    def wrapper(*args, **kwargs):
        st = datetime.datetime.now()
        res=func(*args, **kwargs)
        result_string=f'Function launched at {st} with result {res}'

        with open("result.txt", "a") as file:
            file.write(result_string)

        return res
    return wrapper
#функция
@test_time
def sum_all_args(*args):
    total_sum = sum(args)
    return total_sum

