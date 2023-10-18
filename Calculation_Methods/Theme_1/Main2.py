
import time

def rowOne(n, x):
    res = 0
    for i in range(1, n + 1, 1):
        res += 1 / (i * (i + x))
        return res

def rowTwo(n ,x):
    res = 0
    for i in range(1, n + 1, 1):
        res += (1 / i) - (1 / (i + x))
        return res

n = int(input("Введите кол-во шагов: "))
start1 = time.perf_counter()
xlist = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for i in range(len(xlist)):
    res1 = rowOne(n, xlist[i])
    res2 = rowOne(n, 1)
finish1 = time.perf_counter()
print(f"Время подсчёта ряда 1 равно {finish1 - start1:f}")

start2 = time.perf_counter()
xlist = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for i in range(len(xlist)):
    res1 = rowTwo(n, xlist[i])
    res2 = rowTwo(n, 1)
finish2 = time.perf_counter()
print(f"Время подсчёта ряда 2 равно {finish2 - start2:f}")

if (finish1 - start1) < (finish2 - start2):
    print("Первый ряд сходится быстрее")
    xlist = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for i in range(len(xlist)):
        res1 = rowOne(n, xlist[i])
        res2 = rowOne(n, 1)
    print("Разность phi_x - phi_1: " + str(res2 - res1))
else:
    print("Второй ряд сходится быстрее")
    xlist = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for i in range(len(xlist)):
        res1 = rowTwo(n, xlist[i])
        res2 = rowTwo(n, 1)
    print("Разность phi_x - phi_1: " + str(res2 - res1))
