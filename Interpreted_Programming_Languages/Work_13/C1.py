
from Shape import Shape

class C1(Shape):
    x2 = 0
    y2 = 0
    title = ""
    s_list = []

    def __init__(self, x1, y1, x2, y2, title):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.title = title

    def square(self, s_list):
        print("Для отрезка невозможно найти площадь!")

    def perimeter(self, s_list):
        print("Для отрезка невозможно найти периметр!")

    def move(self, x, y):
        self.x1 += x
        self.x2 += x
        self.y1 += y
        self.y2 += y
        print("Новое положение отрезка по точкам: (" + str(self.x1) + ", " + str(self.y1) + "),  (" + str(self.x2) + ", " + str(self.y2) + ")")

    def fill(self, color):
        print("Отрезку невозможно задать цвет!")
