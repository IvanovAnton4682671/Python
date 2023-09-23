
# Вариант 25
# На основе данных примеров разработайте ER-диаграмму и собственную базу данных по
# выбранной теме. В созданной базе данных создайте как минимум 10 таблиц. Хотя бы в 1
# таблицу вставьте как минимум 1000 записей. Реализуйте как минимум 50 запросов к
# базе данных (запросы на выборку, обновление и удаление данных).
# 25. Компьютерные занятия: список слушателей курсов, список предметов,
# список преподавателей, журнал учета успеваемости.

import sqlite3
from sqlite3 import Error
import random

global con

def sql_createBaseTables(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Subjects(Id integer PRIMARY KEY AUTOINCREMENT, NameSubject text)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Teachers(Id integer PRIMARY KEY AUTOINCREMENT, SurnameTeacher text, "
                      "NameTeacher text, PatronymicTeacher text, IdSubject integer, FOREIGN KEY (IdSubject) "
                      "REFERENCES Subjects (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Listeners(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener "
                      "text, NameListener text, PatronymicListener text, IdSubject integer, FOREIGN KEY (IdSubject) "
                      "REFERENCES Subjects (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS AcademicRecord(Id integer PRIMARY KEY AUTOINCREMENT, "
                      "SurnameListener text, NameListener text, PatronymicListener text, IdSubject integer, "
                      "Mark integer, FOREIGN KEY (IdSubject) REFERENCES Subjects (Id) ON DELETE CASCADE)")
    con.commit()

def sql_AddingBaseTable(con):
    cursorObj = con.cursor()
    temp_subjects_list = ["C++", "C#", "Java", "Python", "HTML", "CSS", "JavaScript", "Vue", "React", "Angular"]
    for subject in temp_subjects_list:
        cursorObj.execute("INSERT INTO Subjects(NameSubject) VALUES(?)", (subject,))
        #тут subject нужно обернуть в кортеж < не subject, а (subject,)>, иначе будет вставлять прсимвольно
    temp_teachers_list = [("Плюсов", "Антон", "Антонович", 1), ("Шарпов", "Богдан", "Богданович", 2), ("Джавный", "Владислав", "Владиславович", 3), ("Питонный", "Григорий", "Григорьевич", 4), ("Штиэмэльный", "Дмитрий", "Дмитриевич", 5), ("Цэесесов", "Евгений", "Евгеньевич", 6), ("Скриптов", "Ёму", "Ёмович", 7), ("Вью", "Жан", "Жанович", 8), ("Реактивный", "Замир", "Замирович", 9), ("Ангуляров", "Игорь", "Игоревич", 10)]
    cursorObj.executemany("INSERT INTO Teachers(SurnameTeacher, NameTeacher, PatronymicTeacher, IdSubject) VALUES(?, "
                          "?, ?, ?)", temp_teachers_list)
    temp_listeners_list = []
    temp_academicRecord_list = []
    for i in range(1000):
        if i < 100:
            temp_listeners_cort = ["Яковлев" + str(i + 1), "Яков" + str(i + 1), "Яковлевич" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 99 < i < 200:
            temp_listeners_cort = ["Юрьев" + str(i + 1), "Юрий" + str(i + 1), "Юрьевич" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 199 < i < 300:
            temp_listeners_cort = ["Эдиков" + str(i + 1), "Эдик" + str(i + 1), "Эдикович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 299 < i < 400:
            temp_listeners_cort = ["Шольцев" + str(i + 1), "Шольц" + str(i + 1), "Шольцович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 399 < i < 500:
            temp_listeners_cort = ["Чендров" + str(i + 1), "Чендр" + str(i + 1), "Чендрович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 499 < i < 600:
            temp_listeners_cort = ["Цоков" + str(i + 1), "Цок" + str(i + 1), "Цокович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 599 < i < 700:
            temp_listeners_cort = ["Хорков" + str(i + 1), "Хорк" + str(i + 1), "Хоркович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 699 < i < 800:
            temp_listeners_cort = ["Фогелев" + str(i + 1), "Фогель" + str(i + 1), "Фогелевич" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        elif 799 < i < 900:
            temp_listeners_cort = ["Удгартов" + str(i + 1), "Удгарт" + str(i + 1), "Удгартович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
        else:
            temp_listeners_cort = ["Торков" + str(i + 1), "Торк" + str(i + 1), "Торкович" + str(i + 1), random.randint(1, 10)]
            temp_listeners_list.append(temp_listeners_cort)
            temp_academicRecord_cort = list(temp_listeners_cort) + [random.randint(2, 5)]
            temp_academicRecord_list.append(temp_academicRecord_cort)
    cursorObj.executemany("INSERT INTO Listeners(SurnameListener, NameListener, PatronymicListener, IdSubject) "
                          "VALUES(?, ?, ?, ?)", temp_listeners_list)
    cursorObj.executemany("INSERT INTO AcademicRecord(SurnameListener, NameListener, PatronymicListener, IdSubject, "
                          "Mark) VALUES(?, ?, ?, ?, ?)", temp_academicRecord_list)
    con.commit()

def sql_outputBaseTables(con):
    cursorObj = con.cursor()
    print()
    print("Subjects")
    cursorObj.execute("SELECT * FROM Subjects")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Teachers")
    cursorObj.execute("SELECT * FROM Teachers")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Listeners")
    cursorObj.execute("SELECT * FROM Listeners")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("AcademicRecord")
    cursorObj.execute("SELECT * FROM AcademicRecord")
    [print(row) for row in cursorObj.fetchall()]
    con.commit()

def sql_deleteBaseTable(con):
    cursorObj = con.cursor()
    cursorObj.execute("DROP table IF EXISTS Subjects")
    cursorObj.execute("DROP table IF EXISTS Teachers")
    cursorObj.execute("DROP table IF EXISTS Listeners")
    cursorObj.execute("DROP table IF EXISTS AcademicRecord")
    print()
    print("Если Базовые таблицы были, то теперь их нет)")
    con.commit()

def sql_createAdditionalTables(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group1(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group2(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group3(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group4(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group5(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Group6(Id integer PRIMARY KEY AUTOINCREMENT, SurnameListener text, "
                      "NameListener text, PatronymicListener text, IdListener integer, FOREIGN KEY (IdListener) "
                      "REFERENCES Listeners (Id) ON DELETE CASCADE)")
    con.commit()

def sql_AddingAdditionalTable(con):
    cursorObj = con.cursor()
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Яковлев" + str(i + 1), "Яков" + str(i + 1), "Яковлевич" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group1(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Юрьев" + str(i + 1), "Юрий" + str(i + 1), "Юрьевич" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group2(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Эдиков" + str(i + 1), "Эдик" + str(i + 1), "Эдикович" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group3(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Шольцев" + str(i + 1), "Шольц" + str(i + 1), "Шольцович" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group4(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Чендров" + str(i + 1), "Чендр" + str(i + 1), "Чендрович" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group5(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    temp_listeners_list = []
    for i in range(10):
        temp_listeners_cort = ["Цоков" + str(i + 1), "Цок" + str(i + 1), "Цокович" + str(i + 1), i + 1]
        temp_listeners_list.append(temp_listeners_cort)
    cursorObj.executemany("INSERT INTO Group6(SurnameListener, NameListener, PatronymicListener, IdListener) VALUES("
                          "?, ?, ?, ?)", temp_listeners_list)
    con.commit()

def sql_updatingAdditionalTables(con):
    cursorObj = con.cursor()
    temp_update_list = ["Райан", "Томас", "Гослинг"]
    for i in range(11):
        temp_update_list.append(i)
        cursorObj.execute("UPDATE Group1 SET SurnameListener = ?, NameListener = ?, PatronymicListener = ? WHERE Id = ?", temp_update_list)
        temp_update_list.pop(-1)
    con.commit()

def sql_deleteDataFromAdditionalTables(con):
    cursorObj = con.cursor()
    for i in range(11):
        temp_Id = i
        cursorObj.execute("DELETE FROM Group2 WHERE Id = ?", (temp_Id,))
    con.commit()

def sql_outputAdditionalTables(con):
    cursorObj = con.cursor()
    print()
    print("Group1")
    cursorObj.execute("SELECT * FROM Group1")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Group2")
    cursorObj.execute("SELECT * FROM Group2")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Group3")
    cursorObj.execute("SELECT * FROM Group3")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Group4")
    cursorObj.execute("SELECT * FROM Group4")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Group5")
    cursorObj.execute("SELECT * FROM Group5")
    [print(row) for row in cursorObj.fetchall()]
    print()
    print("Group6")
    cursorObj.execute("SELECT * FROM Group6")
    [print(row) for row in cursorObj.fetchall()]
    con.commit()

def sql_deleteAdditionalTables(con):
    cursorObj = con.cursor()
    cursorObj.execute("DROP table IF EXISTS Group1")
    cursorObj.execute("DROP table IF EXISTS Group2")
    cursorObj.execute("DROP table IF EXISTS Group3")
    cursorObj.execute("DROP table IF EXISTS Group4")
    cursorObj.execute("DROP table IF EXISTS Group5")
    cursorObj.execute("DROP table IF EXISTS Group6")
    print()
    print("Если Дополнительные таблицы были, то теперь их нет)")
    con.commit()

#----------------------------------------------------------------------------------------------------#

try:
    con = sqlite3.connect("ComputerClassesDB.db")
except Error:
    print(Error)

sql_createBaseTables(con)
sql_AddingBaseTable(con)
sql_outputBaseTables(con)
#sql_deleteBaseTable(con)
sql_createAdditionalTables(con)
sql_AddingAdditionalTable(con)
sql_outputAdditionalTables(con)
sql_updatingAdditionalTables(con)
sql_deleteDataFromAdditionalTables(con)
print()
print("Таблицы после изменения:")
sql_outputAdditionalTables(con)
#sql_deleteAdditionalTables(con)

con.close()
