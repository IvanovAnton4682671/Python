# n = 10 - вариант

import matplotlib.pyplot as plt
import random
import math
import numpy as np


def task_1():
    # y = f(x), y = 0, x = 0
    n = 10
    x = [i for i in range(21)]
    a, b = [0.0, 20.0], [0.0, 10.0]
    number_of_points = 1000

    def function(array_of_x, number_n):
        array_of_values = []
        for i in range(len(array_of_x)):
            if array_of_x[i] < number_n:
                array_of_values.append((10 * array_of_x[i]) / number_n)
            else:
                try:
                    array_of_values.append(10 * ((array_of_x[i] - 20) / (number_n - 20)))
                except ZeroDivisionError:
                    array_of_values.append(10 * (1 / 1))
        return array_of_values

    def graph(array_of_x, array_of_y, array_points):
        plt.plot(array_of_x, array_of_y, label="1", color="gray")
        plt.scatter(array_of_x, array_of_y, color="gray", marker="o")
        for i in range(len(array_points)):
            plt.scatter(array_points[i][0], array_points[i][1], color="blue", marker="o")
        plt.title("График функции и случайных точек")
        plt.xlabel("X")
        plt.ylabel("F(x)")
        plt.grid(True)
        plt.show()

    def create_random_points(width, height, number):
        array_of_points = []
        for i in range(number):
            temp_x = random.uniform(0.0, 20.0)
            temp_y = random.uniform(0.0, 10.0)
            temp_tuple = (temp_x, temp_y)
            array_of_points.append(temp_tuple)
        return array_of_points

    y = function(x, n)
    points = create_random_points(a, b, number_of_points)
    graph(x, y, points)

    m = 0
    for i in range(len(points)):
        tmp_x = function([points[i][0]], 20)
        if points[i][1] < tmp_x[0]:
            m += 1
    s = m / number_of_points * len(a) * len(b)
    print("Приближённая площадь фигуры = {}".format(s))

    f_n = function([10], 20)
    f_20 = function([20], 20)
    true_area = ((((10 * f_n[0]) / 2) + ((10 * f_20[0]) / 2)) / (20 - 10)) - ((20 - 10) / 2)
    print("Настоящая площадь = {}".format(true_area))
    print("Абсолютная погрешность = {}".format(abs(true_area - s)))
    print("Относительная погрешность = {}".format(abs((s - true_area) / true_area)))


def task_2():
    n = 10
    a, b = [0.0, 5.0], [0.0, 11.0]
    y_max = 10.9875
    s_ab = math.sqrt(math.pow((0 - 0), 2) + math.pow((5 - 0), 2)) * math.sqrt(math.pow((5 - 5), 2) + math.pow((10.9875 - 0), 2))
    number_of_points = 500

    def function(x, number):
        return 11 - (n * math.pow(math.sin(x), 2))

    def graph(array_points):
        array_of_x = [i for i in range(-100, 101)]
        temp_arr = []
        for i in range(len(array_of_x)):
            temp_arr.append(function(i, n))
        plt.plot(array_of_x, temp_arr, label="1", color="gray")
        for i in range(len(array_points)):
            plt.scatter(array_points[i][0], array_points[i][1], color="blue", marker="o")
        plt.xlabel("X")
        plt.ylabel("F(x)")
        plt.grid(True)
        plt.show()

    def create_random_points(width, height, number):
        array_of_points = []
        for i in range(number):
            temp_x = random.uniform(0.0, 5.0)
            temp_y = random.uniform(0.0, 11.0)
            temp_tuple = (temp_x, temp_y)
            array_of_points.append(temp_tuple)
        return array_of_points

    def new_x(array_points):
        array_of_f = []
        for i in range(len(array_points)):
            array_of_f.append(function(array_points[i][0], n))
        return array_of_f

    points = create_random_points(a, b, number_of_points)
    graph(points)
    array_f = new_x(points) # значения функции в случайных точках
    sred_f = sum(array_f) / len(array_f) # среднее значение функции в случайных точках
    answer = sred_f * s_ab
    print("Площадь прямоугольника, в котором определён интеграл: {}".format(s_ab))
    print("Среднее значение функции в точках: {}".format(sred_f))
    print("Приближённое значение исходного интеграла: {}".format(answer))


def task_3():
    # круг радиуса 10
    n = 10
    number_of_points = 1000
    a, b = [-10.0, 10.0], [-10.0, 10.0]

    def create_round():
        array_of_round_points = []
        for phi in np.linspace(0, 2 * math.pi, 100):
            x = n * math.cos(phi)
            y = n * math.sin(phi)
            array_of_round_points.append((x, y))
        return array_of_round_points

    def create_random_points(width, height, number):
        array_of_points = []
        for i in range(number):
            temp_x = random.uniform(width[0], width[1])
            temp_y = random.uniform(height[0], height[1])
            temp_tuple = (temp_x, temp_y)
            array_of_points.append(temp_tuple)
        return array_of_points

    def points_in_round(array_of_points):
        kol = 0
        for i in range(len(array_of_points)):
            if math.pow(array_of_points[i][0], 2) + math.pow(array_of_points[i][1], 2) <= math.pow(n, 2):
                kol += 1
        return kol

    def graph(array_of_points_round, array_of_random_points):
        tmp_x_r, tmp_y_r = [], []
        for i in range(len(array_of_points_round)):
            tmp_x_r.append(array_of_points_round[i][0])
            tmp_y_r.append(array_of_points_round[i][1])
        plt.plot(tmp_x_r, tmp_y_r, label="1", color="red")
        tmp_x_r, tmp_y_r = [], []
        for i in range(len(array_of_random_points)):
            tmp_x_r.append(array_of_random_points[i][0])
            tmp_y_r.append(array_of_random_points[i][1])
            plt.scatter(tmp_x_r, tmp_y_r, color="blue", marker="o")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

    points_of_round = create_round()
    round_p = create_random_points(a, b, number_of_points)
    graph(points_of_round, round_p)
    kol = points_in_round(round_p)
    my_pi = 4 * (kol / number_of_points)
    print("Кол-во точек, попавших в круг: {}".format(kol))
    print("Приблизительное значение pi: {}".format(my_pi))


def task_4():
    n = 10
    a = 11 + n
    b = 11 - n
    number_of_points = 500
    width, height = [-25.0, 25.0], [-1, 1]

    def create_curve():

        t = np.linspace(0, 2 * np.pi, 1000)
        x = a * np.cos(t)
        y = b * np.sin(t)
        return x, y

    def create_random_points(width, height, number):
        array_of_points = []
        for i in range(number):
            temp_x = random.uniform(width[0], width[1])
            temp_y = random.uniform(height[0], height[1])
            temp_tuple = (temp_x, temp_y)
            array_of_points.append(temp_tuple)
        return array_of_points

    def graph(x, y, array_of_points):
        x_r, y_r = [], []
        for i in range(len(array_of_points)):
            x_r.append(array_of_points[i][0])
            y_r.append(array_of_points[i][1])
        plt.plot(x, y, label="1", color="red")
        plt.scatter(x_r, y_r, color="blue", marker="o")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

    def points_inside_ellipse(a, b, point_array):
        center_x = 0
        center_y = 0

        inside_count = 0
        for point in point_array:
            x, y = point[0] - center_x, point[1] - center_y
            if (x / a) ** 2 + (y / b) ** 2 <= 1:
                inside_count += 1
        return inside_count

    def ellipse_area(a, b):
        return math.pi * a * b

    def mc_estimate(a, b, num_points, width, height):
        points = create_random_points(width, height, num_points)
        count_inside = points_inside_ellipse(a, b, points)
        rectangle_area = (width[1] - width[0]) * (height[1] - height[0])
        return rectangle_area * (count_inside / num_points)

    x, y = create_curve()
    curve_points = list(zip(x, y))
    random_points = create_random_points(width, height, number_of_points)
    graph(x, y, random_points)
    print("Настоящая площадь эллипса: {}".format(ellipse_area(a, b)))
    print("Количество точек в эллипсе: ", points_inside_ellipse(a, b, random_points))
    print("Приблизительная площадь эллипса: {}".format(mc_estimate(a, b, number_of_points, width, height)))


#task_1()
#task_2()
#task_3()
#task_4()
