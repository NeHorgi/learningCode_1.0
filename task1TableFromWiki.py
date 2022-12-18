'''
Данный код написан мною для преобразования таблицы с веб-страницы википедии и создания объекта-таблицы,
с целью его последующего использования в параметрезированном
тесте, который должен проверять, что в таблице в столбце "Popylarity" нет значений меньше передаваемого.
'''


from dataclasses import dataclass, field, fields
from typing import List, Any

from bs4 import BeautifulSoup
import requests
import lxml


url = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')
soup = BeautifulSoup(url.text, "html.parser")
wiki_table = soup.table

#Наша будущая таблица с необходимыми данными и метод для ее выведения
result = []

def show_result():
    for row in result:
        print(row)


'''
Здесь мы пишем цикл, который из исходной таблицы с веб-страницы 
сформирует нам новую таблицу, куда будут входить только необходимые нам значения 
'''


for string_num in range(1, 16):                                 #Для каждой строки таблицы (всего их 15)
    string = []                                                 #Список для формирования строки
    string_tags = wiki_table.find_all('tr')[string_num]         #Присваиваем переменной все элементы первой строки с тэгом 'tr'
    for column_num in range(4):                                 #Для каждого столбца таблицы (всего нам нужных первые 4)
        column_tags = string_tags.find_all('td')[column_num]    #Присваиваем переменной элемент столбца таблицы с тэгом 'td'
        string.append(column_tags)                              #Добавляем элемент столбца в формирующуюся "строку" будущей таблицы
    result.append(string)                                       #Добавляем сформированную строку таблицы в новую таблицу


'''
Здесь будет очень много циклов по преобразованию таблицы с вики в более читабельный и
значительно легче обрабатываемый формат
'''


#Преобразуем первый элемент таблицы в название вебсайта
for string in result:
    first_elem = string[0]
    title = first_elem.find('a').string
    string[0] = title

#Преобразуем третий элемент таблицы в список языков, используемых во фронт-энде
for string in result:
    third_elem = string[2]
    title = third_elem.find_all('a')
    string[2] = []
    for elem in title:
        string[2].append(elem.string)

#Преобразуем четвертый элемент таблицы в список языков, используемых в бэк-энде
for string in result:
    fouth_elem = string[3]
    title = fouth_elem.find_all('a')
    string[3] = []
    for elem in title:
        string[3].append(elem.string)

#Преобразуем второй элемент таблицы, убирая тэги и все лишнее, используя метов get_text()
for string in result:
    second_elem = string[1]
    text = second_elem.get_text()
    result_text = ''
    for letter in text:
        if letter in ' [':
            break
        else:
            result_text += letter
    string[1] = result_text.rstrip()

#Преобразуем четвертый элемент таблицы, убирая из него ненужные гипер-ссылки
for string in result:
    new_string = []
    for language in string[3]:
        language.get_text()
        for letter in language:
            if letter in '[]':
                break
            else:
                new_string.append(language)
                break
    string[3] = new_string

#Преобразуем второй элемент таблицы, избавляясь от запитых в числе
for string in result:
    result_number = ''
    for number in string[1]:
        if number == ',':
            result_number += '_'
        else:
            result_number += number
    string[1] = result_number

#И, наконец, преобразуем второй элемент таблицы в число
for row in result:
    row[1] = int(row[1])


'''
Реализация датаклассов для хранения данных из таблицы.
Представлены три датакласса:
urlWikiTable - для хранения html таблицы 
fullWikiTable - для хранения преобразованной целой таблицы 
companyInfo - для хранения каждого элемента таблицы
'''


@dataclass
class urlWikiTable:
    url: Any = wiki_table


@dataclass(eq=False)
class fullWikiTable:
    table: List = field(default_factory=list)


@dataclass(eq=False)
class companyInfo:
    row: List = field(default_factory=list)








