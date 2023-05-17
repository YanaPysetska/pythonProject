from HW_10 import sum_all_args
if __name__ == '__main__':
    result = sum_all_args(1, 2, 3, 4, 5)


from HW_10_2 import complex_operations
if __name__ == '__main__':
    complex_num_1 = complex(3, 4)
    complex_num_2 = complex(2, 1)
    sum_result, sub_result, comparison_result = complex_operations(complex_num_1, complex_num_2)
    print("Результат сложения:", sum_result)
    print("Результат вычитания:", sub_result)
    print("Сравнение комплексных чисел:", comparison_result)