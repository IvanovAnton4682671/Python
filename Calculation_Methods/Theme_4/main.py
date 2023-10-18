
main_matrix = [[12.14, 1.32, -0.78, -2.75],
               [-0.89, 16.75, 1.88, -1.55],
               [2.65, -1.27, -15.64, -0.64],
               [2.44, 1.52, 1.93, -11.43]]
main_answers_array = [14.78, -12.14, -11.65, 4.26]
epsilon = 0.001
initial_approximation = [[0, 0, 0, 0],
                         [1, 1, 1, 1],
                         [2, 2, 2, 2]]

def print_system(matrix, answers_array):
    # вывод
    print("Система:")
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print(" | {}".format(answers_array[i]))

def canonical_form_matrix(matrix, answers_array):
    n = len(matrix)
    for i in range(n):
        # находим максимальный элемент в столбце
        max_element = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k
        # меняем строки местами
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        answers_array[i], answers_array[max_row] = answers_array[max_row], answers_array[i]
    # вывод
    print()
    print("Система после приведения к каноническому виду:")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print(" | {}".format(answers_array[i]))

def formulas_of_the_iterative_process(matrix, answers_array):
    formulas_array = []
    n = len(matrix)
    for i in range(n):
        temp_array = []
        # находим главный коэффицент
        main_ratio = round(1 / matrix[i][i], 5)
        temp_array.append(main_ratio)
        # добавляем ответы
        temp_array.append(answers_array[i])
        # добавляем оставшиеся иксы (меняем знак при переносе через =)
        for j in range(n):
            if i != j:
                temp_array.append(-matrix[i][j])
        # заполняем массив формул
        formulas_array.append(temp_array)
    # вывод
    print()
    print("Вид итерационных формул:")
    for i in range(n):
        print("X{} = {} * ({} + {} + {} + {})".format(i + 1, formulas_array[i][0], formulas_array[i][1],
                                                      formulas_array[i][2], formulas_array[i][3],
                                                      formulas_array[i][4]))
    return formulas_array

def Jakobi(initial_approximation, formulas_array, betta, epsilon, num_approximation):
    # выполняем приближения
    num_approximation += 1
    x_array = initial_approximation
    approximation_array = []
    # вычисляем новые коэффиценты
    x1 = formulas_array[0][0] * (formulas_array[0][1] + x_array[1] + x_array[2] + x_array[3])
    approximation_array.append(x1)
    x2 = formulas_array[1][0] * (formulas_array[1][1] + x_array[0] + x_array[2] + x_array[3])
    approximation_array.append(x2)
    x3 = formulas_array[2][0] * (formulas_array[2][1] + x_array[0] + x_array[1] + x_array[3])
    approximation_array.append(x3)
    x4 = formulas_array[3][0] * (formulas_array[3][1] + x_array[0] + x_array[1] + x_array[2])
    approximation_array.append(x4)
    betta = max(abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3]))
    # если точность меньше эпсилон - вызываем с новыми коэффицентами
    if betta > epsilon:
        results_array = [abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                         abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3])]
        x_array = approximation_array
        print("На шаге {} условие betta <= epsilon не выполнилось, т.к. значения betta: {}".format(
            num_approximation, results_array))
        return Jakobi(x_array, formulas_array, betta, epsilon, num_approximation)
    # иначе - печатаем ответ
    else:
        results_array = [abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                         abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3])]
        return num_approximation, results_array

def Zeidel(initial_approximation, formulas_array, betta, epsilon, num_approximation):
    # выполняем приближения
    num_approximation += 1
    x_array = initial_approximation
    approximation_array = []
    # вычисляем новые коэффиценты
    x1 = formulas_array[0][0] * (formulas_array[0][1] + x_array[1] + x_array[2] + x_array[3])
    approximation_array.append(x1)
    x2 = formulas_array[1][0] * (formulas_array[1][1] + x1 + x_array[2] + x_array[3])
    approximation_array.append(x2)
    x3 = formulas_array[2][0] * (formulas_array[2][1] + x1 + x2 + x_array[3])
    approximation_array.append(x3)
    x4 = formulas_array[3][0] * (formulas_array[3][1] + x1 + x2 + x3)
    approximation_array.append(x4)
    betta = max(abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3]))
    # если точность меньше эпсилон - вызываем с новыми коэффицентами
    if betta > epsilon:
        results_array = [abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                         abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3])]
        x_array = approximation_array
        print("На шаге {} условие betta <= epsilon не выполнилось, т.к. значения betta: {}".format(
            num_approximation, results_array))
        return Zeidel(x_array, formulas_array, betta, epsilon, num_approximation)
    # иначе - печатаем ответ
    else:
        results_array = [abs(approximation_array[0] - x_array[0]), abs(approximation_array[1] - x_array[1]),
                         abs(approximation_array[2] - x_array[2]), abs(approximation_array[3] - x_array[3])]
        return num_approximation, results_array

def base_def():
    print_system(main_matrix, main_answers_array)
    canonical_form_matrix(main_matrix, main_answers_array)

def task():
    main_formulas_array = formulas_of_the_iterative_process(main_matrix, main_answers_array)
    print()
    print("Для метода Якоби:")
    print()
    for i in range(len(initial_approximation)):
        print("Берём начальное приближение: {}".format(initial_approximation[i]))
        num_approximation, approximation_array = Jakobi(initial_approximation[i], main_formulas_array, 1,
                                                        epsilon, 0)
        print("Значения приближения для шага {}, при котором выполнилась точность <= epsilon: {}".format(
            num_approximation, approximation_array))
        print()
    print("Для метода Зейделя:")
    print()
    for i in range(len(initial_approximation)):
        print("Берём начальное приближение: {}".format(initial_approximation[i]))
        num_approximation, approximation_array = Zeidel(initial_approximation[i], main_formulas_array, 1,
                                                        epsilon, 0)
        print("Значения приближения для шага {}, при котором выполнилась точность <= epsilon: {}".format(
            num_approximation, approximation_array))
        print()

base_def()
task()
