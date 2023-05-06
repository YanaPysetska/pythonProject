#файл- создаеться или перезаписываеться
# file=open('hello_world.txt', 'w')
# file.write('Hello world')
import json
import pickle

# file.write('Another word')
# file.close() #нужно закрывать файл обязательно

#Добавление в существующий файл a+ - это чтение и запись
# file=open('hello_world.txt', 'a+')
# file.write('333 Hello world')
# file.close()

#найти конец файла
# file=open('hello_world.txt', 'r+')
# file.seek(0,2)
# file.write('\nMy finale hello world')
# file.close()

#os
# import os
# #текущая дирректория
# current_dir=os.getcwd()
# print(f'My current dirrectory {current_dir}')

#изменить директорию
# os.chdir('..')
# new_current_dir=os.getcwd()
# print(f'My current dirrectory {current_dir}')


# #открываем файл на запись
# file=open("out.txt", "w")
# #записываем что-то в файл:
# file.write("Hello world")
# #обязательно закрываем файл, после того как что-то записали
# file.close()

# #открываем файл на запись(ОТКРЫВАЯ ФАЙЛ НА ЗАПИСЬ УДАЛЯЕМ ПРЕЖНЕЕ СОЖЕРЖИМОЕ)
# file=open("out.txt", "w")
# #записываем что-то в файл:
# file.write("Hello")
# #обязательно закрываем файл, после того как что-то записали
# file.close()

# try:
#     with open("out.txt", "w") as file:
#         file.write("Hello1\n")
#         file.write("Hello2\n")
#         file.write("Hello3\n")
# except:
#     print("Ошибка при работе")

#дозаписать в файл какую-либо инфо:
# try:
#     with open("out2.txt", "a") as file:
#         file.write("Hello1\n")
#         file.write("Hello2\n")
#         file.write("Hello3\n")
# except:
#     print("Ошибка при работе")

#не можем читать данные из файла который открыт на ДОЗАПИСЬ и на ЗАПИСЬ
# try:
#     with open("out2.txt", "a") as file:
#         s=file.readlines()#чтение файла
# except:
#     print("Ошибка при работе")

#a+ означает что мы можем и добалять данный файл и считывать:
# try:
#     with open("out2.txt", "a+") as file:
#         file.seek(0) #ставим файловую позицию чтобы ЧИТАТЬ сначала
#         s=file.readlines()#чтение файла
#         print(s)
# except:
#     print("Ошибка при работе")

#файловая позиция ДЛЯ ЗАПИСИ:
# try:
#     with open("out2.txt", "a+") as file:
#         file.seek(0) #ставим файловую позицию чтобы ЧИТАТЬ сначала
#         file.write("hello4") #записываем данные в КОНЕЦ
#         s=file.readlines()#чтение файла
#         print(s)
# except:
#     print("Ошибка при работе")

#Записываем несколько строк:
# try:
#     with open("out2.txt", "a+") as file:
#         file.seek(0) #ставим файловую позицию чтобы ЧИТАТЬ сначала
#         file.writelines(["Test1\n", "Test2\n"]) #записываем 2 строки
#         s=file.readlines()#чтение файла
#         print(s)
# except:
#     print("Ошибка при работе")

#БИНАРНЫЙ режим доступа:
# books=[
#     ("Гоголь Моголь", "М.В. Золина", 200),
#     ("Воголь Поголь", "А.В. Полина", 250),
#     ("Доголь Роголь", "М.П. Голина", 500),
#     ("Спголь Кроголь", "Р.О. Пердолина", 190)
# ]
# #открываем фал на запись wb
# file=open("out.bin", "wb")
# #для записи нужна библиотека
# pickle.dump(books, file)
# file.close()

# #прочитать коллекцию из файла:
# file=open("out.bin", "rb")
# bs=pickle.load(file)
# file.close()
# print(bs)

#Добавляем несколько записей в бинарный файл:
# books=[("Гоголь Моголь", "М.В. Золина", 200)]
# books2=[("Воголь Поголь", "А.В. Полина", 250)]
# books3=[("Доголь Роголь", "М.П. Голина", 500)]
# books4=[("Спголь Кроголь", "Р.О. Пердолина", 190)]

# try:
#     with open("out.bin","wb") as file:#менеджер контекста
#         pickle.dump(books, file)
#         pickle.dump(books2, file)
#         pickle.dump(books3, file)
#         pickle.dump(books4, file)
# except:
#     print('Ошибка при работе с файлом')

#читаем с файла:
# try:
#     with open("out.bin","rb") as file:#менеджер контекста
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
#         b4 = pickle.load(file)
# except:
#     print('Ошибка при работе с файлом')
# #выводим результат
# print(b1,b2,b3,b4, sep="\n") #ставим перенос строки

#МЕНЕДЖЕР КОНТЕКСТА
#создаем свой класс менеджера контекста который будет менять значения вектора
#если при изменении значения произойдут ошибки - то изменения не внесуться
#а если без ошибок будет измененный

# try:
#     file=open("out2.txt", encoding="utf-8")
#     try:
#         s=file.readlines()
#         int(s) #делаем специально ошибку
#         print(s)
#     finally: #на случай если при чтении возникла ошибка файл нужно закрыть
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")
# #блок для отлова всех исключений:
# except:
#     print("Ошибка при работе с файлом")

#менеджер котекста который нужен для того счтобысократить код
#и чтобы при ошибке чтения - оно всеравно закрывало файл:
# try:
#     with open("out2.txt", encoding="utf-8") as file:
#         s=file.readlines()
#         print(s)
# except FileNotFoundError:
#     print("Невозможно открыть файл")
# #блок для отлова всех исключений:
# except:
#     print("Ошибка при работе с файлом")
# #кусочек который выводит нам то что файл дйствительно закрыт
# finally:
#     print(file.closed)

#генератор
# def get_list():
#     for x in[1,2,3,4]:
#         return x #тут выводиться только 1 значение
# a=get_list()
# print(a)

# чтобы вывести несколько значений, нам нужен оператор yield
# превратили с помощью yield функцию в генератор
# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x
#
# a=get_list()
# for x in a:#перебираем генератор с помощью цыкла:
#     print(x)

#ищем среднее арифметическое сначала от 1-10 потом каждый раз-1
# 1 2 3 4 5 6 7 8 9 10
# 2 3 4 5 6 7 8 9 10
# 3 4 5 6 7 8 9 10
# 4 5 6 7 8 9 10
# 5 6 7 8 9 10
# 6 7 8 9 10
# 7 8 9 10
# 8 9 10
# 9 10

# def get_list():
#     for i in range(1,10):
#         a=range(i, 11)
#         yield sum(a)/len(a)
#
# a=get_list()
# print(list(a))

#есть документ out2.txt - там есть текст, нужно найти индексы слова генератор
#функция для генератора
# def find_word(f,word): #f-ссылка на файл и слово
#     g_indx=0
#     for line in f:
#         indx=0
#         while (indx!=-1):
#             indx=line.find(word, indx)
#             if indx>-1:
#                 yield g_indx+indx
#                 indx+=1
#         g_indx+=len(line)
#
#
# try:
#     with open("out2.txt") as file:
#         a=find_word(file, "Test2") #первый аргумент - функция. вторым аргументом  засовываем строку которую будем искать
#         print(list(a))#выводим списко всех найденных индексов слова генератор
# except FileNotFoundError:
#     print("Файл не найден")
# except:
#     print("Ошибка  обработки файла")


#json - данные в формате ключ значение
#из json - в питоновские обьекты:
# import json #импортируем встроенный модуль
# str_json="""
# {
# "members": {
#     "count":12,
#     "items":[{
#        "name": "Molecule Man",
#        "age": 29,
#        "secretIdentity": "Dan Jukes"
#     },{
#        "name": "Madame Uppercut",
#        "age": 39,
#        "secretIdentity": "Jane Wilson"
#     },{
#        "name": "Eternal Flame",
#        "age": 1000000,
#        "secretIdentity": "Unknown"
#         }]}
# }"""
# # print(type(str_json))
# # #метод куда  передаем строку
# data=json.loads(str_json)
# # print(data)# можно теперь с data работать как со словарем
# # print(data["members"]) #обращамся по этому ключу
# # print(type(data["members"]["items"]))#обращаемся к последнему рядку перед списком уц него будет тип ЛИТС
# #эелементы спсика можно обойти цыклом for
# for i in data["members"]["items"]:
#     #print(i)# из-за фигруных скобок понятно что это словари
#     #мы можем обращаться по ключам:
#     print(i['name'],i['age'])

# #создаем собственную Json:
# my_json="""
# {
# "members": {
#     "count":12,
#     "items":[{
#        "name": "Molecule Man",
#        "age": 29,
#        "secretIdentity": "Dan Jukes"
#     },{
#        "name": "Madame Uppercut",
#        "age": 39,
#        "secretIdentity": "Jane Wilson"
#     },{
#        "name": "Eternal Flame",
#        "age": 1000000,
#        "secretIdentity": "Unknown"
#         }]}
# }"""
#
#
# from random import randint
# from datetime import datetime
# #удаляем клюбч "secretIdentity":
# data=json.loads(my_json)
# for i in data["members"]["items"]:
#     del i["secretIdentity"]#тут удалили
#     i['likes']=randint(100,200)#добавляем новый рандомайзером
#     i['a']=None
#     i['now']=datetime.now().strftime('%d/%m/%y') #дату Json не понимает  поэтому ее с помощью strftime - преобразорвали в строку
#
# print(data["members"]["items"])
#когда мы удалили что-то и добавили новый ключ, формируем свою json
#indent=2- показывает отступы
# new_json=json.dumps(data,indent=2)
# print(new_json)
#
# print(json.loads(new_json))
#json.dump(data["members"]["items"])
#СОХРАНИЛИ СВОЙ json
# with open('my.json','w') as file:
#     json.dump(data,file,indent=3)

#Открываем свой собсвтенный файл на чтение:
# with open('my.json','r') as file:
#     data=json.load(file)
# print(data)


#рекукрсия - функция вызывает сама себя
#глуюина функции - нужно устанавливать условия прерывания
#
# def recursive(value):
#     print(value)
#     if value<4: #установили глубину
#         recursive(value+1)
#     print(value) #
#recursive(1)

#вычисление факториала:
# def fact(n):
#     if n<=0:
#         return 1
#     else:
#         return n*fact(n-1)#fact(n-1) -этот кусок кода и являеться рекрсивной функцией
# p=fact(7)
# print(p)

#ПРИМЕР РЕКУРСИИ С ОБХОДОМ КАТАЛОГОВ И ФАЙЛОВ:

F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'Matlab': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zopfldr.dll']
        }
    }
}
#path - ссылка на словарь depth - глубина обхода
def get_files(path, depth=0):
    for i in path:
        print(""*depth, i)
        if type(path[i])==dict:
            get_files(path[i], depth+1)
        else:
            print(" "*(depth+1)," ".join(path[i]))

get_files(F)