
# Вариант 8
# Разработайте UML-диаграмму и программу. Напишите иерархию геометрических фигур
# с родительским классом Shape и 3 дочерними классами C1, C2 и C3. Базовый класс
# содержит координаты одной точки для вывода фигур на экран и методы square() и
# perimeter(), которые подсчитывают площадь и периметр фигуры соответственно, move(),
# fill() – для сдвига и заливки фигуры цветом, compare(x, y) – для сравнения фигур
# x и y по площади,  is_intersect(x, y) – для определения факта пересечения фигур x и y,
# is_include(x, y) – определяет факт включения y в x. Дочерние классы (отрезок, треугольник,
# четырехугольник, параллелограмм, трапеция, прямоугольник, ромб, квадрат, правильный
# пятиугольник) должны содержать параметры фигуры, по которым их можно нарисовать и
# рассчитать площадь и периметр. Создайте список из 15 объектов дочерних классов.
# Здесь допускаются одинаковые объекты. Выведите на экран величины площади, периметра,
# цвета заливки для всех объектов, попарно сравните фигуры по площади, определите факты
# пересечения фигур и включения. В список вносите программно только уникальные объекты.
# C1 - отрезок, С2 - параллелограмм, С3 - трапеция

from C1 import C1
from C2 import C2
from C3 import C3

def get_unique_obj(obj_list, unique_shapes):
    for obj in obj_list:
        is_unique = True
        for other_obj in obj_list:
            if obj == other_obj:
                continue
            is_field_unique = True
            for field in vars(obj):
                if getattr(obj, field) == getattr(other_obj, field):
                    is_field_unique = False
                    break
            if not is_field_unique:
                is_unique = False
        if is_unique:
            unique_shapes.append(obj.title)
    return unique_shapes


f_list = []
n = int(input("Введите кол-во фигур: "))
for i in range(n):
    s = int(input("1 - отрезок, 2 - параллелограмм, 3 - трапеция: "))
    if s == 1:
        print("Введите параметры для создания отрезка (x1, y1, x2, y2, title):")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        title = input("title: ")
        otr = C1(x1, y1, x2, y2, title)
        f_list.append(otr)
    elif s == 2:
        print("Введите параметры для создания параллелограмма (x1, y1, x2, y2, x3, title):")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        x3 = int(input("x3: "))
        title = input("title: ")
        par = C2(x1, y1, x2, y2, x3, title)
        f_list.append(par)
    elif s == 3:
        print("Введите параметры для создания трапеции (x1, y1, x2, y2, x3, title):")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        x3 = int(input("x3: "))
        title = input("title: ")
        trap = C3(x1, y1, x2, y2, x3, title)
        f_list.append(trap)

for i in range(len(f_list)):
    if isinstance(f_list[i], C1):
        continue
    else:
        c = input("Введите цвет: ")
        f_list[i].fill(c)
        print("Теперь у фигуры " + str(f_list[i].title) + " " + str(f_list[i].color) + " цвет")

for i in range(len(f_list)):
    if isinstance(f_list[i], C1) == False:
        print("Площадь фигуры " + str(f_list[i].title) + ":")
        print(f_list[i].square(f_list[i].s_list))
        print("Периметр фигуры " + str(f_list[i].title) + ":")
        print(f_list[i].perimeter(f_list[i].s_list))
        print("Цвет фигуры " + str(f_list[i].title) + ":")
        print(f_list[i].color)
    else:
        continue

var = 3
print("Перед выводом площадей, пересечений и включений можете побаловаться!")
while var != 0:
    if var == 1:
        print("Список всех фигур:")
        for i in range(len(f_list)):
            print(str(f_list[i].title))
        tmp_s = input("Введите название фигуры, которую хотите подвинуть: ")
        x = int(input("На сколько подвинуть по Х: "))
        y = int(input("На сколько подвинуть по У: "))
        try:
            for i in range(len(f_list)):
                if tmp_s == f_list[i].title:
                    f_list[i].move(x, y)
        except:
            print("Вы ввели неправильное название!")
        var = int(input("0 - выйти из цикла, 1 - подвигать фигуры, 2 - поменять цвет фигурам: "))
    elif var == 2:
        print("Список всех фигур:")
        for i in range(len(f_list)):
            print(str(f_list[i].title))
        tmp_s = input("Введите название фигуры, которую хотите подвинуть: ")
        c = input("Введите цвет, который хотите поставить фигуре: ")
        try:
            for i in range(len(f_list)):
                if tmp_s == f_list[i].title and isinstance(f_list[i], C1) == False:
                    f_list[i].color(c)
                    print("Теперь у фигуры " + str(f_list[i].title) + " " + str(f_list[i].color) + " цвет")
        except:
            print("Вы ввели неправильное название или выбрали отрезок!")
        var = int(input("0 - выйти из цикла, 1 - подвигать фигуры, 2 - поменять цвет фигурам: "))
    else:
        var = int(input("0 - выйти из цикла, 1 - подвигать фигуры, 2 - поменять цвет фигурам: "))

print("Площади, пересечения, включения (попарно):")
for i in range(len(f_list)):
    if isinstance(f_list[i], C1) == False:
        while i < len(f_list) - 1:
            f_list[i].compare(f_list[i], f_list[i + 1])
            f_list[i].is_intersect(f_list[i], f_list[i + 1])
            f_list[i].is_include(f_list[i], f_list[i + 1])
            i += 1
    else:
        i += 1

print("Уникальные фигуры:")
c1_shapes = []
c2_shapes = []
c3_shapes = []
unique_shapes = []
for obj in f_list:
    if isinstance(obj, C1):
        c1_shapes.append(obj)
    elif isinstance(obj, C2):
        c2_shapes.append(obj)
    else:
        c3_shapes.append(obj)
unique_shapes = get_unique_obj(c1_shapes, unique_shapes)
unique_shapes = get_unique_obj(c2_shapes, unique_shapes)
unique_shapes = get_unique_obj(c3_shapes, unique_shapes)
for obj in unique_shapes:
    print(obj)
