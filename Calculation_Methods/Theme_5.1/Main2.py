
import math as mt
import numpy as np
import matplotlib.pyplot as plt

def build_cubic_spline(x, y):
    # определяем кол-во точек интерполяции n и вычисляем массив h (дистанции между соседнимим точками Х)
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    # вычисляем alpha через h и исходными y
    alpha = [(3 * (y[i + 1] - y[i]) / h[i]) - (3 * (y[i] - y[i - 1]) / h[i - 1]) for i in range(1, n - 1)]
    # массивы для дальнейших вычислений
    l = [1] + [0] * (n - 1)
    mu = [0] * n
    z = [0] * n
    c = [0] * n
    # для каждой точки Х вычисляются выражения через h и alpha
    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
    # обновляем значения на границе диапазона данных
    l[n - 1] = 1
    z[n - 1] = 0
    c[n - 1] = 0
    # обратный проход (обновляем значения C и вычисляем b и d для каждого сплайна)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
    b = [(y[i + 1] - y[i]) / h[i] - (h[i] * (c[i + 1] + 2 * c[i])) / 3 for i in range(n - 1)]
    d = [(c[i + 1] - c[i]) / (3 * h[i]) for i in range(n - 1)]
    # создаём список сплайнов через lambda-функцию (каждый сплайн сопоставляется
    # с сегментом между парой соседних точек Х)
    splines = []
    for i in range(n - 1):
        # тут PyCharm видит ошибку, но код работает. Это происходит (скорее всего) из-за того,
        # что PyCharm не может правильно определить контекст для этой операции
        # тут каждая lambda-функция возвращает для себя своё i (можно записать как lambda i: lambda x_val:...)
        spline = lambda x_val, i=i: y[i] + b[i] * (x_val - x[i]) + c[i] * (x_val - x[i]) ** 2 + d[i] * (x_val - x[i]) ** 3
        splines.append(spline)
    return splines

def print_spline_values(x, splines, num=10):
    # вывод сплайнов для диапазона Х-ов (от 2 до 3, от 3 до 5, от 5 до 7)
    for i in range(len(splines)):
        x_values = np.linspace(x[i], x[i + 1], num)
        y_values = [splines[i](x_value) for x_value in x_values]
        print(f"Сплайн {i + 1}:")
        for x_val, y_val in zip(x_values, y_values):
            print(f"x: {x_val:.2f}, y: {y_val:.2f}")
        print("\n")


def plot_splines(x, splines, num=10):
    # создание графика сплайнов
    for i in range(len(splines)):
        x_values = np.linspace(x[i], x[i + 1], num)
        y_values = [splines[i](x_value) for x_value in x_values]
        plt.plot(x_values, y_values, label=f"Сплайн {i + 1}")
    plt.legend()
    plt.grid(True)
    plt.show()

def task_1():
    # диапазон, в котором будем искать все значения - [-1, 1]
    x_array = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0,
               0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    y_array = [1 / (1 + 25 * mt.pow(x, 2)) for x in x_array]
    # делим на два отрезка
    x1_array, x2_array = x_array[:11], x_array[11:]
    y1_array, y2_array = y_array[:11], y_array[11:]
    # создаём сплайны для каждого отрезка
    splines1 = build_cubic_spline(x1_array, y1_array)
    splines2 = build_cubic_spline(x2_array, y2_array)
    # выводим значения сплайнов
    print_spline_values(x1_array, splines1)
    print_spline_values(x2_array, splines2)
    # строим график
    plt.figure(figsize=[10, 5])
    # строим исходную функцию
    plt.plot(x_array, y_array, label='Исходная функция')
    # строим каждый сплайн
    x1_values = np.linspace(x1_array[0], x1_array[-1], 10)
    y1_values = [splines1[-1](x_value) for x_value in x1_values]
    plt.plot(x1_values, y1_values, label='Сплайн 1')
    x2_values = np.linspace(x2_array[0], x2_array[-1], 10)
    y2_values = [splines2[-1](x_value) for x_value in x2_values]
    plt.plot(x2_values, y2_values, label='Сплайн 2')
    plt.legend()
    plt.grid(True)
    plt.show()

def task_2():
    # создаём кубический сплайн для данной табличной функции
    x = [2, 3, 5, 7]
    y = [4, -2, 6, -3]
    splines = build_cubic_spline(x, y)
    print_spline_values(x, splines)
    plot_splines(x, splines)

task_1()
task_2()
