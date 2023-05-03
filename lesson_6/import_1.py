#пакет - набор методов и функций который можем использовать
#показывают рандомные числа
import random
print(random.randint(12, 123))

my_list=[1, 2, True, 65]
print(random.choice(my_list))

#пакетный менеджер которые позволяет загрузить пакеты
#pip list  в терминале

#dir - покажет методы котоыре сетьс в пакете
print(dir(random))

#конструкция
import random
def print_hi():
    print('Hi')
if __name__=='__main__':
    print(random.randint(12,123))
    my_list=[1,2,True,65]
    print(random.choice(my_list))
    print(type(random))
