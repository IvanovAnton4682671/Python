
from math import *

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

a = float(input("Введите коэффицент а: "))
b = float(input("Введите коэффицент b: "))
c = float(input("Введите клэффицент c: "))
global x1, x2

print("Ваше уравнение: (" + str(a) + ")x^2 + (" + str(b) + ")x + (" + str(c) + ") = 0")

d = pow(b, 2) - (4 * a * c)
if d < 0:
    print("Дискриминант меньше 0, корней нет (есть, но мы их не считаем).")
elif d == 0:
    print("Вычисление через дискриминант:")
    x1 = ((-b) + sqrt(d)) / (2 * a)
    print("Дискриминант равен 0, корни: х1 = х2 = " + str(x1))
    print()
    print("Вычисление через сигнум:")
    x1 = -(b + (sign(b) * sqrt(d))) / (2 * a)
    print("Дискриминант равен 0, корни: х1 = х2 = " + str(x1))
else:
    x1 = ((-b) + sqrt(d)) / (2 * a)
    x2 = ((-b) - sqrt(d)) / (2 * a)
    print("Дискриминант больше 0, корни : x1 = " + str(x1) + ", x2 = " + str(x2))
    print()
    print("Вычисление через сигнум:")
    x1 = -((b + (sign(b) * sqrt(d))) / (2 * a))
    x2 = c / (a * x1)
    #x2 = -((b - (sign(b) * sqrt(d))) / (2 * a))
    print("Дискриминант больше 0, корни : x1 = " + str(x1) + ", x2 = " + str(x2))
