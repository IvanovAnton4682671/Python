
# Реализовать заполнение матрицы произвольного размера (nxm) числами в порядке возрастания
# по побочным диагоналям со следующим условием: a00 = 1, anm = n * m.
# Пример:     1 2 4
#             3 5 7
#             6 8 10
#             9 11 12

print("Введите размерность матрицы nxm (n - строки, m - столбцы):")
n = int(input())
m = int(input())

# создаем матрицу из нулей размером nxm
matrix = [[0 for j in range(m)] for i in range(n)]

# заполняем матрицу по побочным диагоналям
num = 1
for diag in range(n + m - 1):
    for i in range(n):
        j = diag - i
        if 0 <= j < m:
            matrix[i][j] = num
            num += 1

# выводим матрицу на экран
for row in matrix:
    print(" ".join(str(elem) for elem in row))
