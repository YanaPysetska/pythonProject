# СТРОКИ
# a='Hello'
# b='Ukraine'
#
# print(a+b)
# print (a*3)

#f -srting
# name ="John"
# age=18
# print(f'My name is {name} and my age {age}')

#convertation
# a=98#int
# b=2.2#float
# c=True#bool
# print(type(str(a)))
# print(type(str(b)))
# print(type(str(c)))

#konkat
# age=23
#
# print('Myname is John ' + str(age) + ' age old')

#поиск подсроки по индексу
# letters='HelloWorld'
# print(letters[2]) #l с начала считате  с 0
# print(letters[-1]) #d с конца считатет см

#slice[start: end: stop: ]
# letters='Hello , World, Lol, glory'
# a=letters[3:] #loWorld
# print(a)
#
# b=letters[3:6] #loW
# print(b)
#
# c=letters[::2] #Hlool тут поставили шаг
# print(c)
#
# len() #кол элементов в нашем рядке

# print(len(letters))

#split разделяет радок

# print((letters.split(','))) #выводит листом
# print(letters.title()) #каждое слово с большой буквы
# print(letters.lower()) #каждое слово с маленькой буквы
# print(letters.replace('Lol', 'kek')) #заменяет слово

#экранирование
# print("It's a string \"pattern\" ")
#c новой строки \n

# f"string"#формат
# b"byte string"#для декодинга
# r"raw string"#для того чтобы вывести слеши, если мы используем экранирование \n
# path="\\lesson_3\\git.pdf"
# print(path)
# ____________________________________________________________
# ЛИСТЫ содержит эелементы какого угодно типа

# my_list=[1, 2, 3, 'lol', 5.5, True]
# print(type(my_list))
# #достать элемент списка
# print(my_list[0])#1
# #менять элементы списка
# my_list[0]='New'
# print(my_list)
# #кол-во элементов в списке
# print(len(my_list))

# #сделать из слова список
my_string='hello'
my_list=list(my_string)
print(my_list)
# #cделать из списка слова
# auto=['BMW', 'Subaru', 'Audi']
# print(' * '.join(auto))
# #сделать лист в строку -> SPLIT

#обратиться к элементу списка (есть список нужно найти индекс у ауди)
# auto=['BMW', 'Subaru', 'Audi']
# print(auto.index('Audi'))

#найти и заменить в листе
# auto=['BMW', 'Subaru', 'Audi']
# index_value=auto.index('Audi')
# auto[index_value]='Audi test'
# print(auto)
# print(auto.pop()) # убирает последний элемент
# print(auto)
# поиск элемента списка в списке
auto=['BMW', 'Subaru', 'Audi', [1,2,334]]
print(auto[3][2])
#добавить список в список
# auto=['BMW', 'Subaru', 'Audi', [1,2,334]]
# print(auto.append(['Shcoda', 'Lol']))
# print(auto)
#
# auto=['BMW', 'Subaru', 'Audi']
# auto2=['Shcoda', 'Lol']
# auto2.extend(auto)
# print(auto2)
#
# auto2=['BMW', 'Subaru', 'Audi']
# index_from_del=auto2.index('BMW')
# del auto2[index_from_del]
# print(auto2)

#tuple кортеж тот же список но не может меняться (добавит/удалить - нельзя)
# my_tuple=(1, )
# print(type(my_tuple))
# my_tuple=(1)
# print(type(my_tuple))
# my_tuple_2=1,2,4,5
# print(type(my_tuple_2))

#посчитать кол-во элементов
# print(my_tuple_2.count())
