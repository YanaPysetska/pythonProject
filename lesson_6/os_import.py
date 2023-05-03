import os
#показывает цпу на компе
# print(os.cpu_count())

#сделать деррикторию
print(os.mkdir('test'))

#сделать много файлов
# for _ in range(1, 10):
#     print(os.mkdir(f'test_{_}'))

#функция получает все папки и файлы в поточной дерррикторри
print(os.scandir('.'))
for item in os.scandir('.'):
    new_item: os.DirEntry=item
    print(item.name)
    # print(item.path)