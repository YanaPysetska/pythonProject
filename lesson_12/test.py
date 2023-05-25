#регулярные выражения
import re

pattern='This'
my_string='This is my text.Text is good (099)333-33-33'
date_string='12/12/2022'
phone_string='(099)333-33-33'

date_format=r'^[\d.-]+$'
phone_format=r'[\d+\-()]+$'

result=re.match(date_format, date_string)
print(result)

result=re.match(phone_format, phone_string)
print(result)

#match - ищет в рядке
result=re.match(pattern, my_string)
print(result)

#search - по всему рядку ищет
search_result=re.search(phone_format, my_string)
print(search_result)

#find all - все совпадения ищет и засовывает их в лист ['text']
find_all_result=re.findall('text', my_string)
print(find_all_result)

#чтобы is убрать ['Th', ' ', ' my text.Text ', ' good (099)333-33-33']
#maxsplit - сколько раз рубануть
result_split=re.split('is', my_string, maxsplit=1)
print(result_split)

#чтобы заменить слово в тексте
result_sub=re.sub('text', 'python', my_string)
print(result_sub)

#code.tutplus.com - тут найти про регульярные выражения


#шаблон пароля
match_result=re.match('^[a-z0-9A-Z_-]{6-16}$', 'abSd_d-4w')
print(match_result)