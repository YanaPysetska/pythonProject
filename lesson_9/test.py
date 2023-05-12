#модуль даты и времени
import datetime
from datetime import date
#
# #вывести время
# now=datetime.datetime.now()
# print(now)
#
# #вывести дату
# current_date=date.today()
# print(current_date)
#
# current_datetime=datetime.datetime.now()
# current_time=current_datetime.date()
#
# print(current_time)
# print(type(current_time))
#
# #12:35:20
# time_obj=datetime.time(12, 35,20)
# print(time_obj)
#
# #2022-10-20 15:20:20
# date_obj=datetime.datetime(2022, 10, 20, 15, 20, 20)
# print(date_obj)

#узнать разницу между датами 31 days
# date_1=datetime.datetime(2022, 10, 20, 15, 20, 20)
# date_2=datetime.datetime(2022, 11, 20, 15, 20, 20)
# delta=date_2-date_1
# print(delta)
#
# #можем даты сравнивать
# if date_2>date_1:
#     print('Hello')


# # today=datetime.date.today()
# print(f'Our date {date_2}')
# new_date=date_2 + datetime.timedelta(days=7)
# print(f'After 7 minutes {new_date}')

# today=datetime.date.today()
# print(f'Our date {date_2}')
# new_date=today + datetime.timedelta(days=7)
# print(f'After 7 days {new_date}')


#timestamp - кол-во времени от начала
#дата в секундах нужно указывать дату
#используеться для бд
# print(datetime.datetime.timestamp(date_2))

import time
#
# #time.sleep(4)
# localtime=time.localtime()
# print(localtime)
#
# #time.struct=true  показать год:
# print(localtime.tm_year)
#
# #mktime
# mktime=time.mktime(localtime)
# print(mktime)
#
my_date_tuple=(2022, 12, 12, 20, 30, 15, 11, 340, 1)
# sktime=time.mktime(my_date_tuple)
# print(sktime)
#
# #выводит реальную дату
# print(time.asctime())
# print(time.asctime(my_date_tuple))

# localtime=time.localtime()
# time.string=time.strftime('My date %m/%d/%Y, %H:%M:%S', my_date_tuple)
# print(time.string)

# my_date='15 June, 2022, 20:22:40'
# result=time.strptime(my_date, "%d %B, %Y, %H:%M:%S")
# print(result)
# print(type(result))
#
# print(time.asctime(result))

