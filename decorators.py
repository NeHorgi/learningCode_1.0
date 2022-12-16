from typing import List, Any
from datetime import datetime


'''
Задача реализовать декоратор, который будет считать время
работы декорируемой функции и выводить его в формате
ЧЧ:ММ:СС.МС
'''


#Реализация декоратора - берем точку отсчета начала работы функции и после вычитаем ее из того времени,
#которое будет, когда функция закончит работу
def timer(func: Any) -> None:
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper


'''
В качесте "подопытного" взята задача с LeetCode, которая мне компьютер уронила из-за слишком долгого выполнения, 
при первой попытке решить ее.
Само условие звучит следующим образом:

169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n / 2 times. 
You may assume that the majority element always exists in the array.
'''


@timer
def majorityElement(nums: List[int]) -> int:
        set_list = set(nums)
        majority_element = 0
        majority_count = 0
        for element in set_list:
            if nums.count(element) > majority_count:
                majority_count = nums.count(element)
                majority_element = element
        return majority_element


#Достаточно большой массив данных, так как мелкие массивы функция щелкает за доли мили-секунд
check = [i for i in range(1, 10000)]


if __name__ == '__main__':
    print(majorityElement(check))
