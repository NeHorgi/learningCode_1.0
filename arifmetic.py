"""
Задания:

Напишите функцию get_sum(value), принимающую любое значение, и возвращающую
сумму его чисел, если это возможно, и None ,если невозможно.
Пример:
get_sum(123)
>>> 6
(т.е. 1+2+3)

"""


def get_sum(value):
    if not value.isdigit():
        return None
    else:
        count = 0
        for elem in value:
            count += int(elem)
        return count


"""
3. Есть функция:
"""

def add_gold(value):
    if value > 1_000:
        raise RuntimeError('Cannot add so much:( Please mercy!')
    print(f'{value} of gold added:) I am breathtaking!')

"""
Невозможно начислить больше 1000 золота за раз.
Напишите функцию add_some_gold(value), принимающую любое значение, и начислите 
требуемое количество золота используя функцию add_gold.
"""

def add_some_gold(value):
    try:
        add_gold(value)
    except RuntimeError:
        print(f'{value} of gold added:) I am breathtaking!')