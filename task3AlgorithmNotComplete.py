'''
Алгоритмы (Необязательное задание)
• Существует поле клеток размером M*N.
• Каждая клетка может быть либо сушей, либо водой.
• На поле находится плот размером в 1 клетку.
• Плот может двигаться только вверх, вниз, вправо и влево.
• Необходимо реализовать:
• Автогенерацию карты. Доля суши от площади поля - 30%.
Алгоритм генерации – произвольный.
• механизм поиска кратчайшего пути из точки A в точку B
на такой карте.
• Параметры M, N, и координаты точек A и B задаются
пользователем.

Мне показалось, что решить данную задачу можно с помощью ООП и это отличная возможность попрактиковаться.
'''


import random

class Space:

    def __init__(self):
        print(f'Введите значения для границы карты. Например: 10, 10 (Матрица 10х10)')
        self.M = int(input())
        self.N = int(input())
        self.space = []

    #Функция генерации карты
    def create_map(self):
        map = [[0 for i in range(self.N)] for i in range(self.M)]
        land = round(self.M * self.N * 0.3)     #Создаю массив в "островами",
        land_list = [1 for i in range(land)]    #который определит их кол-во на карте
        for row in range(len(map)):
            for column in range(len(map[row])):
                if random.randint(0, 1) == 1:
                    if map[row].count(1) >= round(len(map[0]) / 2):     #Ввожу данное условие, дабы избежать ситуации,
                        continue                                        #когда вся земля будет сконцентрирована в одном месте
                    elif land_list == []:
                        break
                    else:
                        map[row][column] = land_list[-1]
                        land_list.pop()
        self.space = map
        return self.space


    #Метод для вывода карты
    def get_space(self):
        for i in self.space:
            print(i)


    '''
    Функции для ввода координат точек. 
    Я реализовал механизм проверки координат на предмет отсутвия установок точек на суше, так как исходил из того, 
    что плот по суше передвигаться не сможет.
    '''

    def take_A(self):
        print(f'Введите координату точки А. (Например: 5 6 (х - 5, у - 6))')
        print(f'Напоминаю, отсчет в Python идет с 0.')
        self.A = input().split()
        if self.space[int(self.A[0])][int(self.A[1])] == 1:
            print(f'Выберете координату точки в воде.')
            self.take_A()
        else:
            return self.A

    def take_B(self):
        print(f'Введите координату точки В (Например: 7 4 (х - 7, у - 4))')
        print(f'Напоминаю, отсчет в Python идет с 0.')
        self.B = input().split()
        if self.space[int(self.B[0])][int(self.B[1])] == 1:
            print(f'Выберете координату точки в воде.')
            self.take_B()
        else:
            return self.B


    #Преобразование координат из строк в числа
    def int_for_coords(self):
        self.A = [int(i) for i in self.A]
        self.B = [int(i) for i in self.B]
        print(self.A, self.B)
        return self.A, self.B


    #Отрисовка координат на карте (для наглядности)
    def take_coords(self):
        self.space[self.A[0]][self.A[1]] = 'A'
        self.space[self.B[0]][self.B[1]] = 'B'


    '''
    Здесь представлены 4 метода для "передвижения" по карте - из точки A в точку B.
    '''
    def move_rigth(self):
        self.A[1] = self.A[1] + 1
        return self.A

    def move_left(self):
        self.A[1] = self.A[1] - 1
        return self.A

    def move_up(self):
        self.A[0] = self.A[0] - 1
        return self.A

    def move_down(self):
        self.A[0] = self.A[0] + 1
        return self.A


    '''
    Алгоритм поиска кратчайшего пути in progres...
    '''
    def jurney(self):
        count = 0
        while self.A != self.B:
            if self.A[0] < self.B[0]:
                if self.space[self.A[0] + 1][self.A[1]] != 1:
                    self.move_down()
                    count += 1
        return print(count)


space = Space()
space.create_map()
space.get_space()
space.take_A()
space.take_B()
space.int_for_coords()
space.take_coords()
space.get_space()
space.jurney()
