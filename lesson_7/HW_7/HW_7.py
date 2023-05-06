# Открыть файл test_file.csv, прочитать,
# распарсить зп сотрудников в долларах и
# перевести в гривны на текущую дату(курс
# задается отдельной переменной).
# Результат сохранить в новый файл salaries_uah.csv
import csv

grn_rate = float(36.94)

with open('test_file.csv', newline='') as file:
        reader = csv.DictReader(file)
        all_rows_upd=[]
        for row in reader:
                upd_row={}
                for key, value in row.items(): #items -для перебора ключ/знач
                        if key == "":
                                upd_row[key] = value
                        else:
                                upd_row[key]=int(value) * grn_rate
                all_rows_upd.append(upd_row)
# Результат сохранить в новый файл salaries_uah.csv
with open('salaries_uah.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # записываем заголовок
        writer.writerow(all_rows_upd[0].keys())
        # Write data rows
        for row in all_rows_upd:
                writer.writerow(row.values())


# Написать скрипт, который подсчитает количество папок и файлов
# по заданному пути. Если такого нет, то по всей системе
# (/ - для линукс/мак. Диск С - для виндоус).
# Для удобства можно установить граничное значение числа папок
# (и/или файлов), после которого скрипт не будет продолжать работу.
# Среди найденных файлов показать самый большой и самый маленький
# по размеру, а так же с самым длинным и коротким именем.
# Если во время работы скрипт был прерван(KeyboardInterrupt),
# то промежуточные результаты сериализуются в файл и при
# повторном запуске эти пути исключаются из проверки.
import os

max_folders = 10000
max_files = 10000

def count_files_and_folders(directory):
    if not directory:
        directory = 'C:\\'

    num_files = 0
    num_folders = 0
    min_size = float('inf')
    max_size = 0
    min_name = ''
    max_name = ''
    for root, dirs, files in os.walk(directory):
        num_files += len(files)
        num_folders += len(dirs)
        if num_files >= max_files or num_folders >= max_folders:
            break
        for f in files:
            filepath = os.path.join(root, f)
            filesize = os.path.getsize(filepath)
            if filesize < min_size:
                min_size = filesize
                min_name = f
            if filesize > max_size:
                max_size = filesize
                max_name = f

            if len(f) < len(min_name):
                min_name = f
            if len(f) > len(max_name):
                max_name = f

    print(f'Найдено файлов: {num_files}')
    print(f'Найдено папок: {num_folders}')
    print(f'Самый маленький файл ({min_name}): {min_size} байт')
    print(f'Самый большой файл ({max_name}): {max_size} байт')
    print(f'Самое короткое имя файла: {min_name}')
    print(f'Самое длинное имя файла: {max_name}')

count_files_and_folders(input("Введите директорию-> "))

