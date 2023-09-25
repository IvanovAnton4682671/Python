
# Вариант 13
# Задание 13. Родословная: LCA.
# В генеалогическом древе определите для двух элементов их наименьшего общего предка
# (Lowest Common Ancestor). Наименьшим общим предком элементов A и B является такой
# элемент C, что С является предком A, C является предком B, при этом глубина C является
# наибольшей из возможных. При этом элемент считается своим собственным предком. Формат
# входных данных аналогичен предыдущей задаче. Для каждого запроса выведите наименьшего
# общего предка данных элементов.

kol_pair = int(input("Введите величину древа (вы введёте на 1 меньше пар): "))

# temp_list_pot = temp_list_rod = [] - не множественное присваивание, а создание фактически одного объекта
temp_list_pot = []
temp_list_rod = []
if kol_pair < 2:
    print("Не удалось создать древо.")
else:
    for i in range(kol_pair - 1):
        s = input("Введите пару (потомок родитель): ")
        temp_list = s.split()
        temp_list_pot.append(temp_list[0])
        temp_list_rod.append(temp_list[1])
    tree = dict(zip(temp_list_pot, temp_list_rod))

    temp_list_ves_1 = []
    temp_list_ves_2 = []
    kol_req = int(input("Введите кол-во запросов на LCA: "))
    for i in range(kol_req):
        s = input("Введите пару, предка которых нужно найти: ")
        temp_list = s.split()
        for key in tree:
            if temp_list[0] in tree:
                temp_list_ves_1.append(key)
            if temp_list[1] in tree:
                temp_list_ves_2.append(key)
        if temp_list_ves_1[::(-1)] == temp_list_ves_2[::(-1)]:
            print(str(tree[temp_list_ves_1[(-1)]]))
