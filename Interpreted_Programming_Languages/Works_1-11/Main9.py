
# Вариант 1
# Задание 1. Максимум.
# Найдите индексы первого вхождения максимального элемента. Выведите два числа:
# номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца. Программа получает
# на вход размеры массива 𝑛 и 𝑚, затем 𝑛 строк по 𝑚 чисел в каждой.

n = int(input("Введите кол-во строк в массиве: "))
m = int(input("Введите кол-во столбцов в массиве: "))
print("Введите сам массив:")
matr = [[int(m) for m in input().split()] for row in range(n)]
for i in range(n):
    if len(matr[i]) < m:
        while len(matr[i]) < m:
            matr[i].append(0)
    if len(matr[i]) > m:
        matr[i] = matr[i][:m]
print("Ваш массив:")
for row in matr:
    for elem in row:
        print(elem, end=' ')
    print()

max_elem = 0
for row in matr:
    for elem in row:
        if elem > max_elem:
            max_elem = elem
print("Все максимальные элементы:")
for i in range(n):
    for j in range(int(len(matr[i]))):
        if matr[i][j] == max_elem:
            print("Номер строки максимального элемента: " + str(i) + ", номер столбца максимального элемента: " + str(j))

count = 0
print("Первое вхождение максимального элемента:")
for i in range(n):
    for j in range(int(len(matr[i]))):
        if count == 0:
            if matr[i][j] == max_elem:
                print("Номер строки максимального элемента: " + str(i) + ", номер столбца максимального элемента: " + str(j))
                count += 1
