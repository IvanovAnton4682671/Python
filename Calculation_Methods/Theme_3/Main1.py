
import math

def my_erf(x):
    erf = 0
    n = 100
    for i in range(1, n + 1):
        erf += (math.pow((-1), i) * math.pow(x, (2 * i) + 1)) / (math.factorial(i) * ((2 * i) + 1))
    erf *= 2 / math.sqrt(math.pi)
    return erf


def gauss(matrix, erf_list):
    n = len(matrix)

    # Прямой ход
    for i in range(n):

        # Находим максимальный элемент в столбце
        max_element = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k

        # Меняем строки местами
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        erf_list[i], erf_list[max_row] = erf_list[max_row], erf_list[i]

        # Обнуляем элементы
        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            erf_list[k] += c * erf_list[i]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = erf_list[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            erf_list[k] -= matrix[k][i] * x[i]

    return x

def to_row_echelon_form(matrix):
    """Приводит расширенную матрицу системы к ступенчатому виду."""
    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    for row in range(rowCount):
        if lead >= columnCount:
            return
        i = row
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = row
                lead += 1
                if lead == columnCount:
                    return
        matrix[i], matrix[row] = matrix[row], matrix[i]
        lv = matrix[row][lead]
        matrix[row] = [mrx / float(lv) for mrx in matrix[row]]
        for i in range(rowCount):
            if i != row:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv*rv for rv, iv in zip(matrix[row], matrix[i])]
        lead += 1
    return matrix

def opr(matrix):
    var1 = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][2] * matrix[1][0] * matrix[2][1] + matrix[2][0] * matrix[0][1] * matrix[1][2]
    var2 = matrix[0][2] * matrix[1][1] * matrix[2][0] + matrix[0][0] * matrix[2][1] * matrix[1][2] + matrix[2][2] * matrix[0][1] * matrix[1][0]
    op = var1 - var2
    if op != 0:
        return 3
    else:
        return 2

def rang(matrix):
    rg = 0
    for row in matrix:
        kol = False
        for element in row:
            if element != 0:
                kol = True
                break
        if kol:
            rg += 1
    return rg

def task_1():
    matrix = [[1.00, 0.80, 0.64], [1.00, 0.90, 0.81], [1.00, 1.10, 1.21]]
    erf_list = [my_erf(0.80), my_erf(0.90), my_erf(1.10)]
    x1, x2, x3 = gauss(matrix, erf_list)
    print("Значения: X1 = {}, X2 = {}, X3 = {}".format(round(x1, 5), round(x2, 5), round(x3, 5)))
    print("Сравнение: X1 + X2 + X3 = {}; erf(1.0) = {}".format(round(x1 + x2 + x3, 5), round(my_erf(1.0), 5)))

def task_2():
    matrix = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    ans_list = [0.1, 0.3, 0.5]
    dop_matrix = [[0.1, 0.2, 0.3, 0.1], [0.4, 0.5, 0.6, 0.3], [0.7, 0.8, 0.9, 0.5]]
    print("Расширенная матрица после элементарных преобразований:")
    to_row_echelon_form(dop_matrix)
    for row in dop_matrix:
        for elem in row:
            print(elem, end=' ')
        print()
    print("Ранг обычной матрицы: {}".format(opr(matrix)))
    print("Ранг расширеннйо матрицы коэффицентов: {}".format(rang(dop_matrix)))
    print("Так как ранг расширенной матрицы коэффицентов больше ранга исходной матрицы, то, по теореме "
          "Кронекера-Капелли, она имеет множество решений")

task_1()
print()
task_2()
