"""
Задание:

Реализовать 2D-движок, который умеет “рисовать” простейшие двумерные примитивы на экране.

Сам движок должен быть представлен в виде объекта класса Engine2D.
Объект класса имеет поле canvas (холст), представленное в виде list’a.
Движок должен иметь метод публичный метод add, принимающий объект произвольной фигуры и добавляющий ее на холст (Canvas).
Реализовать классы для 3-х геометрических фигур:
Окружность - задается координатой центра и радиусом.
Треугольник - задается тремя точками
Прямоугольник - задается точкой нижнего левого угла и длинами сторон a, b
Каждая фигура должна иметь метод draw(), при вызове которого выводится информация в виде print’а, например “Drawing Circle: (0, 1) with radius 5”.
При завершении добавления фигур, у движка необходимо вызвать публичный метод draw(), который последовательно вызовет методы для отрисовки у всех фигур на холсте и очистит его.
"""


class Engine2D:

    def __init__(self):
        self.canvas = []

    def add(self, obj):
        self.canvas.append(obj)

    def draw(self):
        for obj in self.canvas:
             obj.draw()
        self.canvas = []


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self):
        return print(f'Drawing Circle: {self.center} with radius {self.radius}')


class Triangle:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def draw(self):
        return print(f'Drawing Triangle: {self.A}, {self.B} and {self.C}')


class Square:

    def __init__(self, spot, a, b):
        self.spot = spot
        self.a = a
        self.b = b

    def draw(self):
        return print(f'Drawing Square: low-left spot is {self.spot} with {self.a} and {self.b} sides')