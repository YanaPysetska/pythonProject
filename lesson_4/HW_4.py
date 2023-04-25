#Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
# перетворити рядок, щоб кожне ім'я явно починалися з великої літери.
my_list = ["john", "marta", "james", "amanda", "marianna"]
title_list = []
for i in my_list:
    title_list.append(i.title())
print(title_list)

#Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
# Виведіть імена в консолі, кожен з нового рядка, вирівнюючи праву сторону,
# використовуючи метод рядка та форматування через F String.
# Також над іменами першим рядком виведіть NAME, де NAME має бути посередині(string.center()),
# а решта простору заповнена символом "*"
friends_list=["John", "Marta", "James", "Amanda", "Marianna"]
for i in friends_list:
    print("{:*^20s}".format("NAME"))
    print("{:>8}".format(i))

#У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

my_list = ["FirstItem", "FriendsList", "MyTuple"]
new_list = []
for i in my_list:
    new_list.append(i[0].lower() + i[1:])

my_string=' '.join(new_list)
new_string = ""
for char in my_string:
    if char.isupper():
        new_string += "_" + char.lower()
    else:
        new_string += char

snace_case=new_string.split(' ')
print(snace_case)


#Створіть словник з чотирма назвами мов програмування (ключі) та
# іменами розробників цих мов (значення). Виведіть по черзі для усіх елементів
# словника повідомлення типу My favorite programming language is Python. It was created
# by Guido van Rossum. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.
dict_sample={ "Python":"Guido Van Rossum", "Java":"James Gosling","C++":"Bjarne Stroustrup", "JavaScript":"Brendan Eich"}
for k, v in dict_sample.items():
    print(f'My favorite programming language is {k}. It was created {v}')

del dict_sample["C++"]
print(dict_sample)


# Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
# Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
# Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова
# та їхній переклад. Виведіть окремо: словник; ключі і значення словника у вигляді списків.
# AG_dict={"stork":"storch", "hawk":"falke", "woodpecker":"specht", "owl":"eule"}
# print("Виведіть німецький варіант слова owl-> ", AG_dict["owl"])

AG_dict["suffer"] = "leiden"
AG_dict["ignorance"] = "Ignoranz"
print(AG_dict)
keys = AG_dict.keys()
values = AG_dict.values()
print(keys)
print(values)


# Створіть багаторівневий словник subjects навчальних предметів. Використайте наступні
# рядки для ключів верхнього рівня: 'science', 'humanities' і 'public'.
# Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі 'physics',
# 'computer science' і 'biology'. Зробіть так, щоб ключ 'physics' посилався на список рядків
# зі значеннями 'nuclear physics', 'optics' і 'thermodynamics'.
# Решта ключів повинні посилатися на порожні словники.
# Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].

subjects={"science":{"physics":{"nuclear physics", "optics", "thermodynamics"}}, "computer science":{}, "biology":{}}
for i in subjects["science"]:
 print('Ключі subjects ->', i)

print('Значення subjects:')
for i in subjects ["science"]["physics"]:
    print(i)

# Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.
list_numbers=[x+1 for x in range(15)]
print(list_numbers)
list_square = [x**2 for x in list_numbers]
print(list_square)
new_dict=dict(zip(list_numbers,list_square))
print(new_dict)

