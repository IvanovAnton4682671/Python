
import math as mt
import time


def task_1():
    print("--- Задание №1 ---")

    # начальные данные: f(x, y) = 2/sqrt(pi) * e^(-(x^2)), y_0 = 0, x_0 = 0
    def function(x):
        return 2/(mt.sqrt(mt.pi)) * mt.pow(mt.e, -mt.pow(x, 2))
    y_0 = 0
    x_0 = 0

    # будем решать методом Эйлера, а для него нужны h и кол-во шагов
    h = 0.1
    num_steps = 20  # именно 20, потому что нужно от 0.0 до 2.0

    start = time.perf_counter_ns()

    # сам метод Эйлера
    def method_euler(func, y0, x0, h, num_steps):
        res_x, res_y = [], []

        # отдельно обрабатываем для х = 0
        res_x.append(x0)
        res_y.append(y0)

        # остальные случаи
        for _ in range(num_steps):
            x0 += h
            y0 += h * func(x0)
            res_x.append(round(x0, 1))
            res_y.append(round(y0, 3))
        return res_x, res_y

    end = time.perf_counter_ns()

    # ответ
    result_x, result_y = method_euler(function, y_0, x_0, h, num_steps)
    print(f"Метод Эйлера занял {end - start} наносекунд")
    print("Таблица полученных значений:")
    for i in range(len(result_y)):
        print(f"Для x = {result_x[i]} значение y = {result_y[i]}")

    start_2 = time.perf_counter_ns()

    def integrate_rectangle(f, a, b, n, c):
        h = (b - a) / n
        integral_value = 0
        for j in range(n):
            x_j = a + j * h
            integral_value += (c * f(x_j)) * h
        return integral_value

    end_2 = time.perf_counter_ns()

    def task_1_1():
        print()
        # подготовка массива значений Х и константы
        x_list = []
        i = 0
        while i < 2.1:
            x_list.append(round(i, 1))
            i += 0.1
        const = 2 / mt.sqrt(mt.pi)

        # функция интегрирования
        def func(x):
            return mt.pow(mt.e, (-1) * mt.pow(x, 2))

        # метод прямоугольников (f - функция интегрирования, a - нижний предел, b - верхний предел,
        # n - кол-во прямоугольников)
        results = []
        for i in range(len(x_list)):
            results.append(round(integrate_rectangle(func, 0, x_list[i], 1000, const), 3))

        print(f"А метод прямоугольников занял {end_2 - start_2} наносекунд")
        print("Таблица полученных значений:")
        for i in range(len(x_list)):
            print(f"Для х = {x_list[i]} значение функции erf = {results[i]}")

    task_1_1()


def task_2():
    print()
    print("--- Задание №2 ---")
    # начальные условия: dr/dt = 2r - arf, r(0) = r_0; df/dt = -f + arf, f(0) = f_0
    # t - время, r = r(t) - число кроликов, f = f(t) - число лис, a - +const

    # математическая модель
    def function_1(a, r, f):
        return 2 * r - a * r * f

    def function_2(a, r, f):
        return -f + a * r * f

    t_0 = 0
    h = 1
    num_steps = 20

    def method_euler(func1, func2, a, t0, r0, f0, h, num_steps):
        res_t, res_r, res_f = [], [], []
        for _ in range(num_steps):
            t0 += h
            r0, f0 = r0 + h * func1(a, r0, f0), f0 + h * func2(a, r0, f0)
            # f0 += h * func2(a, r0, f0)
            res_t.append(t0)
            res_r.append(r0)
            res_f.append(f0)
        return res_t, res_r, res_f

    def func_answer():
        result_t, result_r, result_f = method_euler(function_1, function_2, a, t_0, r_0, f_0, h, num_steps)
        for j in range(len(result_t)):
            print(f"Значение r = {result_r[j]} и f = {result_f[j]} для t = {result_t[j]}")

    print("Пункт а)")
    a = 0.01
    r_0, f_0 = [2, 3, 10, 100, 500, 1000, 2000, 5000, 10000], [2, 3, 10, 100, 500, 1000, 2000, 5000, 10000]
    for i in range(len(r_0)):
        result_t, result_r, result_f = method_euler(function_1, function_2, a, t_0, r_0[i], f_0[i], h, num_steps)
        print(f"Значения для r_0 и f_0 = {r_0[i]}")
        for j in range(len(result_t)):
            print(f"Значение r = {result_r[j]} и f = {result_f[j]} для t = {result_t[j]}")
    print("Пункт б)")
    a = 0.01
    r_0, f_0 = 15, 22
    print(f"Значения для r_0 = {r_0} и f_0 = {f_0}")
    func_answer()
    r_0, f_0 = 1, 70
    print(f"Лисы вымирают при r_0 = {r_0} и f_0 = {f_0}")  # несколько шагов подряд кол-во лис < 1
    func_answer()
    r_0, f_0 = 10, 10
    a = 0.29
    print(f"Обы вида вымирают при r_0 = f_0 = {r_0}")  # кроме 0 для a = 0.01 не нашёл значения
    func_answer()  # оба вида вымирают при r_0 = f_0 = 10 и a = 0.29


task_1()
task_2()
