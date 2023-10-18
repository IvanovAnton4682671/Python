
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
        node = temp_list[0]
        temp_list_ves_1.clear()
        while node in tree:
            temp_list_ves_1.append(tree.get(node))
            node = tree[node]
            print("ves_1")
            print(temp_list_ves_1)
            print()
        node = temp_list[1]
        temp_list_ves_2.clear()
        while node in tree:
            temp_list_ves_2.append(tree.get(node))
            node = tree[node]
            print("ves_2")
            print(temp_list_ves_2)
            print()
        common_ancestor = None
        # temp_list_ves_1 = temp_list_ves_1[::(-1)]
        # temp_list_ves_2 = temp_list_ves_2[::(-1)]
        # for n1, n2 in zip(temp_list_ves_1, temp_list_ves_2):
        #     if n1 == n2:
        #         common_ancestor = n1
        #     else:
        #         break
        if temp_list_ves_1[::(-1)] == temp_list_ves_2[::(-1)]:
            common_ancestor = temp_list_ves_1[(-1)]
        if common_ancestor is not None:
            print(str(common_ancestor))
        else:
            print("Нет общего предка.")
        # for key in tree:
        #     if temp_list[0] in tree:
        #         temp_list_ves_1.append(key)
        #         print("ves_1")
        #         print(temp_list_ves_1)
        #         print()
        #     if temp_list[1] in tree:
        #         temp_list_ves_2.append(key)
        #         print("ves_2")
        #         print(temp_list_ves_2)
        #         print()
        # if temp_list_ves_1[::(-1)] == temp_list_ves_2[::(-1)]:
        #     print(str(tree[temp_list_ves_1[(-1)]]))
