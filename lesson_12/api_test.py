from pprint import pprint

import requests


URL='https://reqres.in/'
#
# get_result=requests.get(URL+ 'api/users?page=2')
# #Принтим статус код <Response [200]>
# print(get_result.status_code)
# print(get_result)
#
# #для того чтобы результат вывести в красивом виде json
# pprint(get_result.json())

#Делаем метод POST
#В него мы должны епередать данные (data)
DATA={
    "name": "morpheus",
    "job": "leader"
}

post_result=requests.post(URL + 'api/users', data=DATA)
#Принтим статус код <Response [200]>
print(post_result.status_code)
print(post_result)
#для того чтобы результат вывести в красивом виде json
pprint(post_result.json())