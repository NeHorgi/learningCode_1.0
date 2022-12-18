'''
Задание:
1. pytest:
• На сайте
https://en.wikipedia.org/wiki/Programming_languages_used_in_most
_popular_websites
есть таблица «Programming languages used in most popular
websites»
• Необходимо реализовать параметризованный тест,
проверяющий, что в этой таблице нет строк, у которых значение
в столбце «Popularity(unique visitors per month)» меньше
передаваемого в качестве параметра в тест значения.
• Если такие строки в таблице есть, тест выводит сообщение об
ошибке, перечисляя строки с ошибками в виде, пример:
“Yahoo (Frontend:JavaScript|Backend:PHP) has 750000000 unique
visitors per month. (Expected less than 500000)”
• Тест должен запускаться для значений: [10^7, 1.5 * 10^7, 5 *
10^7, 10^8, 5 * 10^8, 10^9, 1.5 * 10^9]
• При реализации теста необходимо учитывать, что данные из этой
таблицы могут понадобиться и в других тестах. Будет плюсом
реализовать хранение данных из таблицы в виде датаклассов.
'''


import task1TableFromWiki
import pytest


nums = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 10 ** 9, 1.5 * 10 ** 9] #Тестовые значения
wiki_table = task1TableFromWiki.result


#Инициализация фикстуры для возможности проэтерироваться по каждому элементу преобразованной таблицы
@pytest.fixture(params=wiki_table)
def wiki_rows(request):
    return request.param


#Функция для инициализации текстого сообщения для тестов
def id_func(test_data, num):
    return f"{test_data[0]} (Frontend:{test_data[2]}|Backend:{test_data[3]}) has {test_data[1]} unique visitors per month. (Expected more than {num})"


@pytest.mark.parametrize('num', nums)
def test_popylarity(wiki_rows, num):
    assert int(num) > int(wiki_rows[1]), id_func(wiki_rows, num)




