#dict  ключ-значение
#
# my_dict={'name':'John', 'age':23, 'books':['Pyrhon', 'Java'], 'id':True, 'city':'Dnipro'}
# my_dict_2={'city':'Kyiv','conuntry':'Ukr'}

# #обьеденить два словаря
# my_dict_new=my_dict | my_dict_2

#создает пары
# print(list(my_dict.items()))

#когда хочет получить ключ и  убирать
# print(my_dict.pop('city'))

#получат последнее значение из словаря убирает
# print(my_dict.popitem())
# print(my_dict)

#получаем клч-знач 3 раза и удалям
# last_val=my_dict.popitem()
# print(last_val * 3)

# last_val=my_dict.pop('name')
# print(last_val * 3)

#добавить новое знач
# my_dict['zip']='231564'
# print(my_dict)

#удалить из словаря
# del my_dict['zip']
# print(my_dict)

#посмотреть есть ли знач в словаре ключ
# print('age' in my_dict)
#__________________________
#SET - список с уникальными значеними, по индексу обратиться в него нельзя, только если конвертировать в ЛИСТ

# empty_set=set()
# print(type(empty_set))
#
# print(set('my_set_my_set')) #убирает дубликаты и делает уникальный список

#пример убарть лишнее, дубликаты из списка
# my_list=[1,2,3,1,4,5]
# print(list(set(my_list)))

#добавить значение в сет
# my_set_2=empty_set.add(222)
# print(empty_set)

#frozeset- нельзя добавлять
# my_frozeset=frozenset()
# print(type(my_frozeset))

#______________________________

#ЦИКЛЫ

#вывести числа с 1 до 5
# count=1
# while count<=5:
#     print(count)
#     count+=1
#     if count==2:
#         name=(input('Set name:'))
#         print(f'count {count}')
#     else:
#         if name=='Joe':
#             print(f'Hi my name {name}')
#             break
#         print('******')
#     if name=='John'
#         print('Continue')
#         continue
#     print('******')
#     print('******')
#
# print('Finish')
#Дебагер - отладкакода - посмотерть по шагу что за чем происходит.
#Брек поинт - левой кнокпйо мыши по рядку -> нажать на жука рядом с раном

#for - цикл
# print(type(range(5)))
# my_list=[1,2,3,4,5]
# for i in my_list: # послоедовательность от 0 до 5
#     print('Test test('+ str(i)+')')
#
# for i in 'my_list': # пересчитала это слово цыклом
#     print(f'My value is {i}')


# my_dict={'name':'John', 'age':23, 'books':['Pyrhon', 'Java'], 'id':True, 'city':'Dnipro'}
# for i in my_dict: # пересчитала это слово цыклом
#     print(f'My value is {i}')


# for i in range(5, 10): #5-9
#     print(f'my value {i}')

# четные числа в ранге от 60 - 80
# for i in range(60, 81, 2):
#     print(f'my value {i}')

#узнать индексы
# ages=[12,22,31,44,52]
# for index, value in enumerate(ages, 2):
#     print(f'My valuse is {value} and index {index}')
#     if value==31:
#         print(f'Finish, index {index}')

#zip - итерация по нескольким последовательностям
#нужно найти совпадения
# ages=[12,22,31,44,52]
# age_2=[122,212,31,434,765]
# age_3=[122,212,31,434,765]
# for i, j, x in zip(ages,age_2,age_3):
#     print(f'First list {i}, srcond list {j}, third list {x}')
#     if i==j:
#         print('Finish')
#         break

#Лист компрехеншн и дикт компрехеншн
# list_my=[]
# for i in range(8):
#     list_my.append(i**2)
# print(list_my)

#сокращенное записаь предидущейго цыкла
#ЭТО ЛИСТ КОМПРЕХЕНШН
# list_my_new=[x**2 for x in range(8) if x%2==0]
# print(list_my_new)
# print(list_my_new==list_my)


# a=[x**2 if x%2==0 else x**3 for x in range(10)]
# print(a)

#dict компрехеншн

# name={'Test1','Test2','Test3','Test4','Test5'}
# age={122,212,31,434,352}
# # my_dict={name:age for name, age in zip(name, age)}
# # print(my_dict)
#
# new_dict_2=dict(zip(name, age))
# print(new_dict_2)