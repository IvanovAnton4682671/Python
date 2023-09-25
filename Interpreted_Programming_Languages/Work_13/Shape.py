
class Shape:
    x1 = 0
    y1 = 0

    def square(self, s_list):
        print("Требуется переопределение для фигуры!")

    def perimeter(self, s_list):
        print("Требуется переопределение для фигуры!")

    def move(self, x, y):
        print("Требуется переопределение для фигуры!")

    def fill(self, color):
        print("Требуется переопределение для фигуры!")

    def compare(self, x, y):
        try:
            if x.area > y.area:
                print("Площадь фигуры " + str(x.title) + " больше фигуры " + str(y.title))
            elif x.area == y.area:
                print("Фигуры " + str(x.title) + " и " + str(y.title) + " равны по площади")
            else:
                print("Площадь фигуры " + str(x.title) + " меньше фигуры " + str(y.title))
        except:
            print("Данные фигуры нельзя сравнить по площади!")

    def is_intersect(self, x__1, y__1):
        x_list = x__1.s_list
        y_list = y__1.s_list
        x_1 = [x_list[i][0] for i in range(4)]
        y_1 = [x_list[i][1] for i in range(4)]
        x_2 = [y_list[i][0] for i in range(4)]
        y_2 = [y_list[i][0] for i in range(4)]

        min_x1 = min(x_1)
        max_x1 = max(x_1)
        min_y1 = min(y_1)
        max_y1 = max(y_1)

        min_x2 = min(x_2)
        max_x2 = max(x_2)
        min_y2 = min(y_2)
        max_y2 = max(y_2)

        if max_x1 < min_x2 or min_x1 > max_x2:
            print("Фигуры " + str(x__1.title) + " и " + str(y__1.title) + " не пересекаются")
        if max_y1 < min_y2 or min_y1 > max_y2:
            print("Фигуры " + str(x__1.title) + " и " + str(y__1.title) + " не пересекаются")
        print("Фигуры " + str(x__1.title) + " и " + str(y__1.title) + " пересекаются")

    def is_include(self, x__1, y__1):
        x_list = x__1.s_list
        y_list = y__1.s_list
        x_1 = [x_list[i][0] for i in range(4)]
        y_1 = [x_list[i][1] for i in range(4)]
        x_2 = [y_list[i][0] for i in range(4)]
        y_2 = [y_list[i][0] for i in range(4)]

        min_x1 = min(x_1)
        max_x1 = max(x_1)
        min_y1 = min(y_1)
        max_y1 = max(y_1)

        min_x2 = min(x_2)
        max_x2 = max(x_2)
        min_y2 = min(y_2)
        max_y2 = max(y_2)

        if min_x2 >= min_x1 and max_x2 <= max_x1 and min_y2 >= min_y1 and max_y2 <= max_y1:
            print("Фигура " + str(y__1.title) + " включена в фигуру " + str(x__1.title))
        print("Фигура " + str(y__1.title) + " не включена в фигуру " + str(x__1.title))
