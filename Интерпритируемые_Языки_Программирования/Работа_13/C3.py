
from Shape import Shape
from math import *

class C3(Shape):
    x2 = 0
    y2 = 0
    x3 = 0
    title = ""
    y3 = 0
    x4 = 0
    y4 = 0
    area = 0
    color = ""
    s_list = []

    def __init__(self, x1, y1, x2, y2, x3, title):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y2
        self.title = title
        if x2 > x1:
            self.x4 = x3 - x1
            self.y4 = y1
        else:
            self.x4 = x3
            self.y4 = y1
        self.s_list = [(x1, y1), (x2, y2), (x3, self.y3), (self.x4, self.y4)]

    def square(self, s_list):
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]

        area = 0.5 * abs((x_1 - x_2) * (y_3 - y_1) + (x_3 - x_4) * (y_1 - y_2))
        self.area = area
        return self.area

    def perimeter(self, s_list):
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]

        x1_length = sqrt(abs(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)))
        x2_length = sqrt(abs(pow(x_3 - x_2, 2) + pow(y_3 - y_2, 2)))
        x3_length = sqrt(abs(pow(x_4 - x_3, 2) + pow(y_4 - y_3, 2)))
        x4_length = sqrt(abs(pow(x_1 - x_4, 2) + pow(y_1 - y_4, 2)))

        return x1_length + x2_length + x3_length + x4_length

    def move(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y
        self.x3 += x
        self.y3 += y
        self.x4 += x
        self.y4 += y
        print("Новое положение параллелограмма по точкам: (" + str(self.x1) + ", " + str(self.y1) + "), (" + str(self.x2) + ", " + str(self.y2) + "), (" + str(self.x3) + ", " + str(self.y3) + "), (" + str(self.x4) + ", " + str(self.y4) + ")")

    def fill(self, color):
        self.color = color
