# Знайти ідентифікатор групи, де знаходиться найбільша кількість
# жінок, народжених після 1977 року.
# Як відповідь необхідно вказати через пробыл
# ідентифікатор знайденої групи і скільки в ній було
# жінок, народжених після 1977 року. Файл group_people.json

import json

with open('group_people.json') as f:
    file_content = f.read()
    users_list = json.loads(file_content)
print(type(users_list))
print(users_list)

max_year_count = 0
max_year_id = None

for i in users_list:
    year_count = 0
    for person in i['people']:
        if person['year'] > 1977 and person['gender']=='Female':
            year_count += 1
    if year_count > max_year_count:
        max_year_count = year_count
        max_year_id = i['id_group']

print("id_group с наибольшим количеством людей после 1977 года:", max_year_id)

# Знайти найуспішнішого менеджера за підсумковою сумою продажів.
# Як відповідь потрібно через пробыл вказати спершу його ім'я,
# потім прізвище і після загальну суму його продажів.Файл manager_sales.json
with open('manager_sales.json') as f:
    file_content = f.read()
    manager_list = json.loads(file_content)
print(type(manager_list))
print(manager_list)

for manager_cars in manager_list:
    total_price = 0
    for car in manager_cars['cars']:
        total_price += car['price']
    print(f"{manager_cars['manager']['first_name']} {manager_cars['manager']['last_name']} продал машин на сумму {total_price}")