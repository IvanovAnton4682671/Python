
import math
import matplotlib.pyplot as plt


def function(x, a, b):
    try:
        y = round(x * math.sin(a * x) + b, 3)
    except ZeroDivisionError:
        return 0
    return y


def splitting(x_first, x_last, step):
    array_of_values = []
    x = x_first
    array_of_values.append(x_first)
    while x <= x_last:
        x += step
        x = round(x, 1)
        if x <= x_last:
            array_of_values.append(x)
    return array_of_values


def graph(array_of_x, array_of_y, func):
    plt.plot(array_of_x, array_of_y, label="1", color="gray")
    x = array_of_x[::1]
    y = array_of_y[::1]
    plt.scatter(x, y, color="gray", marker="o")

    y_min, y_max = min(array_of_y), max(array_of_y)
    x_min, x_max = 0, 0
    for i in range(len(array_of_x)):
        if y_min == array_of_y[i]:
            x_min = array_of_x[i]
        if y_max == array_of_y[i]:
            x_max = array_of_x[i]
    plt.vlines(x_min, 0, y_min, color="black", linestyles="dashed")
    # ha и va - горизонтальное и вертикальное выравнивание
    plt.text(x_min, 0, str(y_min), ha="right", va="bottom", color="red")
    plt.vlines(x_max, 0, y_max, color="black", linestyles="dashed")
    plt.text(x_max, 0, str(y_max), ha="right", va="top", color="red")

    plt.title("График функции {}".format(func))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


def task():
    func = "y = x * sin(a * x) + b"
    array_of_x = splitting(0.0, 2 * math.pi, math.pi / 10)
    a, b = 0, 0
    f = False
    while not f:
        try:
            tmp_arr = input("Введите коэффиценты a, b через пробел: ").split()
            a, b = float(tmp_arr[0]), float(tmp_arr[1])
            f = True
        except ValueError:
            print("Вы ввели некорректные коэффиценты, попробуйте ещё раз.")
    array_of_y = []
    for x in array_of_x:
        array_of_y.append(function(x, a, b))
    graph(array_of_x, array_of_y, func)


task()
