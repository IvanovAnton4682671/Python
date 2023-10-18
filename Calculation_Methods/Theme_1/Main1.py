
# Ряд Тейлора для функции ошибок

import math

xlist = [0.5, 1.0, 5.0, 10.0]
erf = 0
n = int(input("Введите кол-во операций: "))

for i in range(0, len(xlist), 1):
    for j in range(0, n, 1):
        erf += (math.pow((-1), j) * math.pow(xlist[i], (2 * j) + 1)) / (math.factorial(j) * ((2 * j) + 1))
    erf *= 2 / math.sqrt(math.pi)
    print("Для Х = " + str(xlist[i]) + " и кол-ва операций " + str(n) + " результат: " + str(erf))
    erf = 0
