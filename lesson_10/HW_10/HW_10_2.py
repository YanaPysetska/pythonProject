# Створити декоратор який вимірює час виконання функції
import time
def test_time(func):
    def wrapper(*args, **kwargs):
        st=time.time()
        res=func(*args, **kwargs)
        et=time.time()
        dt=et-st
        print(f'Время работы: {dt} cек')
        return res
    return wrapper

#функция
@test_time
def complex_operations(a, b):
    sum_result = a + b
    sub_result = a - b
    if a == b:
        comparison_result = "Числа равны"
    else:
        comparison_result = "Числа не равны"
    return sum_result, sub_result, comparison_result




