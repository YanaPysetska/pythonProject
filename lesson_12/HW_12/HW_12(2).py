#Уважно вивчіть документацію цього API
# (https://swapi.dev/documentation) і напишіть програму,
# яка виводить на екран (і JSON-файл)
# інформацію про пілотів легендарного корабля Millennium Falcon.
# Інформація про корабель має містити такі пункти:
# назва,
# максимальна швидкість,
# клас,
# список пілотів.
# Усередині списку про кожен пілот має бути така інформація:
# ім'я,
# зріст,
# вага,
# рідна планета,
# посилання на інформацію про рідну планету.
from pprint import pprint
import requests
import json

URL = 'https://swapi.dev/'
name = 'Millennium Falcon'
get_result=requests.get(URL + 'api/starships', params={'search': name})
data=get_result.json()

ship_data = data['results'][0]
ship_info = ['name', 'starship_class', 'max_atmosphering_speed', 'pilots']
extracted_data = {field: ship_data.get(field) for field in ship_info}

pilot_urls = extracted_data['pilots']
pilots_list=[]

for pilot_url in pilot_urls:
    response = requests.get(pilot_url)
    pilot_data = response.json()

    pilot_info = {
        "name" : pilot_data['name'],
        "height" : pilot_data['height'],
        "mass" : pilot_data['mass'],
        "homeworld_url" : pilot_data['homeworld']
    }

    pilots_list.append(pilot_info)

extracted_data['pilots'] = pilots_list
print(json.dumps(extracted_data, indent=4))