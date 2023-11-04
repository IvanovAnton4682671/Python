
import math
import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return 1 / (1 + (25 * math.pow(x, 2)))

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)

    def basis(j, x):
        b = 1
        for i in range(n):
            if i != j:
                b *= (x - x_values[i]) / (x_values[j] - x_values[i])
        return b

    def interpolate(x):
        result = 0
        for j in range(n):
            result += y_values[j] * basis(j, x)
        return result

    interpolated_values = []
    for x_val in x:
        interpolated_values.append(interpolate(x_val))

    return interpolated_values

def lagrange_interpolation_equidistant(x_values, y_values, n):
    x = np.linspace(min(x_values), max(x_values), n)
    return lagrange_interpolation(x_values, y_values, x)

def lagrange_interpolation_chebyshev(x_values, y_values, n):
    x = [0.5 * (max(x_values) + min(x_values)) + 0.5 * (max(x_values) - min(x_values)) * np.cos(
        (2 * i + 1) * np.pi / (2 * n)) for i in range(n)]
    return lagrange_interpolation(x_values, y_values, x)

def graph(x_array, f_array, a_array, b_array, n, name1, name2, name3):
    plt.figure(figsize=(15, 4))

    plt.subplot(131)
    plt.plot(x_array, f_array, label="1", color="blue")
    plt.title(name1)
    plt.xlabel("X")
    plt.ylabel("Функция")
    plt.grid(True)

    plt.subplot(132)
    plt.plot(range(len(a_array)), a_array, label="2", color="red")
    plt.title(name2 + " n = {}".format(n))
    plt.xlabel("X")
    plt.ylabel("Полином")
    plt.grid(True)

    plt.subplot(133)
    plt.plot(range(len(b_array)), b_array, label="3", color="green")
    plt.title(name3 + " n = {}".format(n))
    plt.xlabel("X")
    plt.ylabel("Полином")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def task():
    section = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1,
               0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    array_of_values = []
    for i in range(len(section)):
        array_of_values.append(round(function(section[i]), 5))

    n = [10, 20, 30, 40, 50]
    for i in range(len(n)):
        array_of_interpolated_a = lagrange_interpolation_equidistant(section, array_of_values, n[i])
        array_of_interpolated_b = lagrange_interpolation_chebyshev(section, array_of_values, n[i])
        graph(section, array_of_values, array_of_interpolated_a, array_of_interpolated_b, n[i],
              "Функция", "Равноотстаящие узлы для", "Чебушевские узлы для")
        array_of_deviation_a = []
        array_of_deviation_b = []
        for j in range(len(array_of_values)):
            try:
                array_of_deviation_a.append(round(abs(array_of_values[j] - array_of_interpolated_a[j]), 5))
                array_of_deviation_b.append(round(abs(array_of_values[j] - array_of_interpolated_b[j]), 5))
            except:
                continue
        graph(section, array_of_values, array_of_deviation_a, array_of_deviation_b, n[i],"Функция",
              "Отклонение для равноостаящих узлов", "Отклонение для чебушевских узлов")

task()
