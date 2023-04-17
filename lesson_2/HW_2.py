# 1. Написати програму, яка вміє переводити температуру з C в Фаренгетів і Кельвінів Наприклад: дана температура в Цельсіях 25 С
# Фаренгейт: 45.9F - вважається за формулою (C+32) * 5/9
# Кельвіни: 298.16K - вважається за формулою C + 273.16

celsium =int(input('Enter temperature celsius: '))
fahrenheit = celsium * 9 / 5 + 32
kelvins = celsium+273.15
print(f"fahrenheit -> {fahrenheit}F")
print(f"kelvins -> {kelvins}K")

# 2.Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2.
# Написати програму, яка порахує об'єм і температуру суміші, що вийшла обчислюється за формулою (v1*t1 + v2*t2) / (v1 + v2)
# Всі параметри виводяться в консолі, вивести обьєм та температуру
v1 =int(input('Enter extent water: '))
t1=int(input('Enter temperature: '))
v2 =int(input('Enter second extent water: '))
t2=int(input('Enter second temperature: '))
substance = (v1*t1 + v2*t2) / (v1 + v2)
print(f"Result -> {substance}")

# 3. Написати програму для підрахунку конвертації валюти:
# UAH --> USD
# UAH --> EUR
UAH = float(input('Enter amount of money UAH: '))
print(f'USD= {UAH *0.027}')
print(f'EUR= {UAH *0.025}')
# # USD --> UAH
USD = float(input('Enter amount of money USD: '))
print(f'UAH= {USD *36.76}')
# # EUR --> UAH
EUR = float(input('Enter amount of money EUR: '))
print(f'UAH= {EUR *40.32}')


# 4.Написать калькулятор с основными операциями(+, -, *, /)
# Користувач вводить два числа та арефметичну операцію

def calculator():
    number1=float(input('Enter first number: '))
    number2=float(input('Enter second number: '))
    arithmetic_operation=(input('Enter (+, -, *, /): '))
    if arithmetic_operation=='+':
        pluss=number1+number2
        print(pluss)
    elif arithmetic_operation=='-':
        minus = number1 - number2
        print(minus)
    elif arithmetic_operation == '*':
        multiply = number1 * number2
        print(multiply)
    elif arithmetic_operation == '/':
        division = number1 / number2
        print(division)
    else:
        print('Error')

def user_choise():
    while True:
        a = input("Enter y/n to continue")
        if a == 'y':
            calculator()
        elif a == "n":
            break
        else:
            print("Enter either y/n")
user_choise()
