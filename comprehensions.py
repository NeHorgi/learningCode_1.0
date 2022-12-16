"""
Задания:

В бою находится 3 игрока. Положение игрока на карте описывается тремя координатами
в виде списка [x, y, z]. Центр координат расположен в середине карты. X, y, z в диапазоне от -10 до 10

Необходимо:
1.	Написать функцию generate_coordinates(game_time), принимающую время,
которое игроки должны провести в игре, и возвращающую словарь вида

{время: список координат всех игроков}.

Время изменяется на 1 секунду за раз;
координаты - целые числа, генерируются случайно в разрешённом диапазоне;
игроки могут находиться в одной точке.

2.	Написать функцию extract_coordinates(coordinates),
где coordinates – сгенерированный словарь из generate_coordinates и возвращающую
плоский список неповторяющихся значений координат игроков.

Пример:
coords = generate_coordinates(0)
print(coords)
>>>{0: [[0,1,2], [3,4,5], [6,7,8]]}
extract_coordinates(coords)
>>>[0,1,2,3,4,5,6,7,8]
"""

'''Вот по этому заданию у меня есть вопросы по условию:
1) нужно ли здесть использовать модуль time? Или "время" тут условно 
и просто передается переменная, которая эмитирует время?
2) я написал цикл, который присваивает координаты каждой секунде, 
верно ли я понял задание? 
3) так же, правильно ли я понял, что координаты в каждую секунду времени
могут быть абсолютно рандомными?'''

def generate_coordinates(game_time):
    import random
    result = {}
    for period in range(game_time + 1):
        result[period] = [[random.randint(-10, 10) for i in range(3)] for i in range(3)]
    return result

def extract_coordinates(coordinates):
    result = []
    for value in coordinates.values():
        for items in value:
            for item in items:
                if item not in result:
                    result.append(item)
    return sorted(result)