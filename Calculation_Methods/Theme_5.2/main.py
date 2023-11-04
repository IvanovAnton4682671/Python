
import math
import matplotlib.pyplot as plt
import numpy

def graph():
    def func1(x):
        return 47.23 * x - 6982.06

    def func2(x):
        return 5.1 * (x ** 0.49)

    def func3(x):
        return 0.01 * (math.e ** (-0.04 * x))

    def func4(x):
        return 8 * (x ** 2) - 40.77 * x + 64.74

    x = numpy.linspace(3, 8, 6)

    plt.figure(figsize=(8, 8))

    # тут последняя цифра - номер графика в окне
    plt.subplot(2, 2, 1)
    plt.plot(x, func1(x), label="1", color="red")
    plt.scatter(x, func1(x), color="red", marker="o")
    plt.title("Линейная")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(x, func2(x), label="2", color="green")
    plt.scatter(x, func2(x), color="green", marker="o")
    plt.title("Степенная")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(x, func3(x), label="3", color="blue")
    plt.scatter(x, func3(x), color="blue", marker="o")
    plt.title("Показательная")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(x, func4(x), label="4", color="orange")
    plt.scatter(x, func4(x), color="orange", marker="o")
    plt.title("Квадратичная")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()

def task():
    def task1_1(array_of_x, array_of_y):
        # ищем в виде линейной функции вида y = ax + b

        # находим суммы Xi, Yi, Xi^2 и Xi * Yi
        sum_Xi, sum_Yi, sum_Xi2, sum_XiYi = 0, 0, 0, 0

        for i in range(len(array_of_x)):
            sum_Xi += array_of_x[i]
            sum_Yi += array_of_y[i]
            sum_Xi2 += math.pow(array_of_x[i], 2)
            sum_XiYi += array_of_x[i] * array_of_y[i]

        # наша система
        sys_1 = [sum_Xi2, sum_Xi, sum_XiYi]
        sys_2 = [sum_Xi, 6, sum_Yi]

        # решаем методом Крамера
        delta = sys_1[0] * sys_2[1] - sys_1[1] * sys_2[0]
        delta_1 = sys_1[2] * sys_2[1] - sys_1[1] * sys_2[2]
        delta_2 = sys_1[0] * sys_2[2] - sys_1[2] * sys_1[0]

        a = round(delta_1 / delta, 2)
        b = round(delta_2 / delta, 2)

        return a, b

    def task1_2(array_of_x, array_of_y):
        # ищем в виде степенной функции вида y = betta * x^alpha

        # сводим к линейной функции вида ln_y = a * ln_x + ln_betta
        new_array_of_x = [math.log(math.e, x) for x in array_of_x]
        new_array_of_y = [math.log(math.e, y) for y in array_of_y]

        # решаем как задачу 1
        a, b = task1_1(new_array_of_x, new_array_of_y)

        # находим betta
        betta = round(math.pow(math.e, b), 2)

        return betta, a

    def task1_3(array_of_x, array_of_y):
        # ищем в виде показательной функции вида y = betta * exp^(a * x)

        # сводим к линейной функции вида ln_y = a * x + ln_betta
        new_array_of_y = [math.log(math.e, y) for y in array_of_y]

        # решаем как задачу 1
        a, b = task1_1(array_of_x, new_array_of_y)

        # находим betta
        betta = math.pow(math.e, b)

        return betta, a

    def task1_4(array_of_x, array_of_y):
        # ищем в виде квадратичной функции вида y = a * x^2 + b * x + c

        # находим суммы Xi4, Xi3, Xi2, Xi, Xi2 * Yi, Xi * Yi и Yi
        sum_Xi4, sum_Xi3, sum_Xi2, sum_Xi, sum_Xi2Yi, sum_XiYi, sum_Yi = 0, 0, 0, 0, 0, 0, 0

        for i in range(len(array_of_x)):
            sum_Xi4 += math.pow(array_of_x[i], 4)
            sum_Xi3 += math.pow(array_of_x[i], 3)
            sum_Xi2 += math.pow(array_of_x[i], 2)
            sum_Xi += array_of_x[i]
            sum_Xi2Yi += math.pow(array_of_x[i], 2) * array_of_y[i]
            sum_XiYi += array_of_x[i] * array_of_y[i]
            sum_Yi += array_of_y[i]

        # наша система
        sys_1 = [sum_Xi4, sum_Xi3, sum_Xi2, sum_Xi2Yi]
        sys_2 = [sum_Xi3, sum_Xi2, sum_Xi, sum_XiYi]
        sys_3 = [sum_Xi2, sum_Xi, 6, sum_Yi]

        # решаем методом Крамера
        delta = (sys_1[0] * sys_2[1] * sys_3[2] + sys_1[2] * sys_2[0] * sys_3[1] + sys_1[1] * sys_2[2] * sys_3[0] -
                 sys_1[2] * sys_2[1] * sys_3[0] - sys_1[0] * sys_2[2] * sys_3[1] - sys_1[1] * sys_2[0] * sys_3[2])
        delta_1 = (sys_1[3] * sys_2[1] * sys_3[2] + sys_1[2] * sys_2[3] * sys_3[1] + sys_1[1] * sys_2[2] * sys_3[3] -
                   sys_1[2] * sys_2[1] * sys_3[3] - sys_1[3] * sys_2[2] * sys_3[1] - sys_1[1] * sys_2[3] * sys_3[2])
        delta_2 = (sys_1[0] * sys_2[3] * sys_3[2] + sys_1[2] * sys_2[0] * sys_3[3] + sys_1[3] * sys_2[2] * sys_3[0] -
                   sys_1[2] * sys_2[3] * sys_3[0] - sys_1[0] * sys_2[2] * sys_3[3] - sys_1[3] * sys_2[0] * sys_3[2])
        delta_3 = (sys_1[0] * sys_2[1] * sys_3[3] + sys_1[3] * sys_2[0] * sys_3[1] + sys_1[1] * sys_2[3] * sys_3[0] -
                   sys_1[3] * sys_2[1] * sys_3[0] - sys_1[0] * sys_2[3] * sys_3[1] - sys_1[1] * sys_2[0] * sys_3[3])

        a = round(delta_1 / delta, 2)
        b = round(delta_2 / delta, 2)
        c = round(delta_3 / delta, 2)

        return a, b, c

    array_of_x = [3, 4, 5, 6, 7, 8]
    array_of_y = [13, 31, 64, 105, 170, 252]

    a, b = task1_1(array_of_x, array_of_y)
    print("Линейная функция: y = ({}) * x + ({})".format(a, b))

    betta, a = task1_2(array_of_x, array_of_y)
    print("Степенная функция: y = ({}) * x^({})".format(betta, a))

    betta, a = task1_3(array_of_x, array_of_y)
    print("Показательная функция: y = ({}) (это значение такое маленькое, что если округлить до 0.01 - получится 0.0)"
          " * exp^({} * x)".format(betta, a))

    a, b, c = task1_4(array_of_x, array_of_y)
    print("Квадратичная функция: y = ({}) * x^2 + ({}) * x + ({})".format(a, b, c))

    graph()

task()
