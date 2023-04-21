#Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
polindrom =input('Enter word ->: ')
if polindrom==polindrom[::-1]:
    print('+')
else:
    print('-')

#Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'
text =input('Enter text ->: ')
list_creat = text.split(' ')
search_word=input('Enter word for searching ->: ')
if search_word in list_creat:
    print('YES')
else:
    print('NO')

#Користувач водить рядок. Якщо він починається на 'abc', замінити їх на 'www',  інакше додати в кінець рядка 'zzz'.
text =input('Enter text line->: ')
if text[0:3]=='abc':
    print(text.replace('abc', 'www'))
else:
    add_zzz=text+'zzz'
    print(add_zzz)


#Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити,що в пошті є символ '@' і '.',
# і якщо це так, вивести "YES", інакше "NO"
email =input('Enter an email->: ')
if '@' in email and '.' in email:
    print("YES")
else:
    print("NO")

#Користувач водить текст через пробіл. Конвертувати текст у список. Вивести остані 3 елементи зі списку, якщо список містить менше 3-х
# елементів,вивести повідомлення про те що кількість елементів менша за 3 і вказати кількість елементів поточного списку
text2 =input('Enter text with spaces->: ')
text2_list=(text2.split(' '))
if len(text2_list)>=3:
    new_list=text2_list[-3:]
    print(new_list)
else:
    print('the number of elements is less than 3, the number of items in the current list', len(text2_list))

