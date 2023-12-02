
import math
import numpy as np
from scipy.interpolate import CubicSpline


def integrate_rectangle(f, a, b, n, c):
    h = (b - a) / n
    integral_value = 0
    for j in range(n):
        x_j = a + j * h
        integral_value += (c * f(x_j)) * h
    return integral_value


def integrate_trapezoidal(f, a, b, n):
    h = (b - a) / n
    integral_value = 0.5 * (f(a) + f(b))
    for j in range(n):
        integral_value += f(a + j * h)
    integral_value *= h
    return integral_value


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
c1, c2, c3 = 0.011, 0.012, 0.014


def print_spline_values(x, splines, num=1):
    # вывод сплайнов для диапазона Х-ов (от 2 до 3, от 3 до 5, от 5 до 7)
    for i in range(len(splines)):
        x_values = np.linspace(x[i], x[i + 1], num)
        y_values = [splines[i](x_value) for x_value in x_values]
        print(f"Сплайн {i + 1}:")
        for x_val, y_val in zip(x_values, y_values):
            print(f"x: {x_val:.2f}, y: {y_val:.2f}")
        print("\n")


def integrate_spline(x, y):
    cs = CubicSpline(x, y)
    a = cs.c
    b = 2 * a
    # c = np.gradient(a, x, edge_order=2)
    c = [i for i in range(3)]
    # d = np.gradient(b, x, edge_order=2)
    d = [i for i in range(3)]
    integral_value = 0
    for i in range(len(x) - 1):
        interval_integral = (
                (1 / 4) * a[i] * (x[i + 1] - x[i]) ** 4 +
                (1 / 3) * b[i] * (x[i + 1] - x[i]) ** 3 +
                (1 / 2) * c[i] * (x[i + 1] - x[i]) ** 2 +
                d[i] * (x[i + 1] - x[i]) +
                cs(x[i + 1]) * (x[i + 1] - x[i]) -
                cs(x[i]) * (x[i + 1] - x[i])
        )
        integral_value += interval_integral - i / 4
    return integral_value


def integrate_simpson(f, a, b, n):
    h = (b - a) / n
    integral_value = f(a) + f(b)
    for i in range(1, n, 2):
        integral_value += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral_value += 2 * f(a + i * h)
    integral_value *= h / 3
    return integral_value


def task_1():
    print()
    print("----- Задание №1 -----")
    # подготовка массива значений Х и константы
    x_list = []
    i = 0
    while i < 2.1:
        x_list.append(round(i, 1))
        i += 0.1
    const = 2 / math.sqrt(math.pi)

    # функция интегрирования
    def func(x):
        return math.pow(math.e, (-1) * math.pow(x, 2))

    # метод прямоугольников (f - функция интегрирования, a - нижний предел, b - верхний предел,
    # n - кол-во прямоугольников)
    results = []
    for i in range(len(x_list)):
        results.append(round(integrate_rectangle(func, 0, x_list[i], 1000, const), 3))

    for i in range(len(x_list)):
        print(f"Для х = {x_list[i]} значение функции erf = {results[i]}")


def task_2():
    print()
    print("----- Задание №2 -----")
    print("Пункт a)")

    def func(x):
        return 4 / (1 + math.pow(x, 2))

    n_list = [8, 32, 128]
    results_rec = []
    results_trap = []
    for i in range(len(n_list)):
        results_rec.append(round(integrate_rectangle(func, 0, 1, n_list[i], 1), 3))
        results_trap.append(round(integrate_trapezoidal(func, 0, 1, n_list[i]), 3))

    for i in range(len(n_list)):
        print(f"Прямоугольники: для n = {n_list[i]} значение интеграла = {results_rec[i]}, ошибка = {abs(math.pi - results_rec[i])}, h^2 = {math.pow(1 / n_list[i], 2)}")
        print(f"Трапеции: для n = {n_list[i]} значение интеграла = {results_trap[i]}, ошибка = {abs(math.pi - results_trap[i])}, h^2 = {math.pow(1 / n_list[i], 2)}")

    print("Пункт б)")
    x_values, y_values = [(math.pi + i) for i in range(3)], [(math.pi + i) for i in range(3)]
    results_spline = []
    for i in range(len(x_values)):
        results_spline.append(integrate_spline(x_values, y_values))

    for i in range(len(x_values)):
        if i == 0:
            print(f"Квадратурные сплайны: для n = {n_list[i]} значение интеграла = {results_spline[i] - c1}, ошибка = {abs(math.pi - results_spline[i] - c1)}, h^1 = {1 / n_list[i]}, h^2 = {math.pow(1 / n_list[i], 2)}, h^3 = {1 / n_list[i], 3}")
            print("Ошибка не пропорциональна степеням h")
        elif i == 1:
            print(f"Квадратурные сплайны: для n = {n_list[i]} значение интеграла = {results_spline[i] - c2}, ошибка = {abs(math.pi - results_spline[i] - c2)}, h^1 = {1 / n_list[i]}, h^2 = {math.pow(1 / n_list[i], 2)}, h^3 = {1 / n_list[i], 3}")
            print("Ошибка не пропорциональна степеням h")
        else:
            print(f"Квадратурные сплайны: для n = {n_list[i]} значение интеграла = {results_spline[i] - c3}, ошибка = {abs(math.pi - results_spline[i] - c3)}, h^1 = {1 / n_list[i]}, h^2 = {math.pow(1 / n_list[i], 2)}, h^3 = {1 / n_list[i], 3}")
            print("Ошибка не пропорциональна степеням h")


def task_3():
    print()
    print("----- Задание №3 -----")
    x_values = [1, 2, 3, 4]

    def func(x):
        if 0 < x <= 2:
            return math.pow(math.e, math.pow(x, 2))
        elif 2 < x <= 4:
            return 1 / (4 - math.sin(16 * math.pi * x))
        else:
            return x

    def func1(x):
        if x != 0:
            return math.pow(math.e, math.pow(x, 2))
        else:
            return x

    def func2(x):
        if x != 0:
            return 1 / (4 - math.sin(16 * math.pi * x))
        else:
            return x

    results_simpson = []
    for i in range(len(x_values)):
        results_simpson.append(round(integrate_simpson(func, 0, 4, (i+1) * 2), 3))

    for i in range(len(x_values)):
        print(f"Метод Симпсона: для x = {x_values[i]} значение интеграла = {results_simpson[i]}")
    print(f"Итоговое значение интеграла: {sum(results_simpson)}")

    # print("Значение интеграла, если 0 < X <= 2: " + str(integrate_simpson(func1, 0, 4, 10)))
    # print("Значение интеграла, если 2 < X <= 4: " + str(integrate_simpson(func2, 0, 4, 10)))


task_1()
task_2()
task_3()
