# short_list=[1,2,3]
#
# my_index=5


#
# try:
#     print(short_list[my_index])
# except: #позвоялет выполянть что-то если ошибка илим для отлова выйняткив
#     print(f"Need position in range {len(short_list)}")

class OrderCountError(Exception):
    pass
orders=[1,2,3,5]
if len(orders)<10:
    raise OrderCountError
#показать експешн красиво

# try:
#     print(1/0)
# except IndexError:
#     print(f'Index Error')
# except ZeroDivisionError as zero:
#     print(f'My error {zero}')

# try:
#     print(1/0)
# except IndexError:
#     print(f'Index Error')
# else:
#     print('Else block')
# finally:
#     print('Finaly')



