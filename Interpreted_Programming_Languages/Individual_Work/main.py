
import itertools
import time

base_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
             "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
             "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25}

def word_generator(alphabet):
    # генерация всех возможных перестановок в строке
    return itertools.permutations(alphabet, len(alphabet))

def word_verification_1(input_s):
    # проверка слова на уникальность (должно состоять из 25 различных букв)
    temp_set = set(list(input_s))
    if len(temp_set) == 25:
        return 1
    else:
        return 0

def word_verification_2(input_s):
    # проверка слова на корректность (должно выполняться условие, что каждая последующая буква
    # в строке и в столбце должна стоять дальше в алфавите, чем предыдущая (таблица 5х5))
    temp_table = [[0 for j in range(5)] for i in range(5)]
    n = len(temp_table)
    count = 0
    for i in range(n):
        for j in range(n):
            temp_table[i][j] = input_s[count]
            count += 1
    #print(temp_table)
    f = True
    for i in range(5):
        for j in range(5):
            try:
                if (base_dict.get(temp_table[i][j]) > base_dict.get(temp_table[i][j + 1])) or (base_dict.get(temp_table[i][j]) > base_dict.get(temp_table[i + 1][j])):
                    f = False
                    break
            except:
                continue
    if f == True:
        return 1
    else:
        return 0

def create_data_file():
    # постепенная запись подходящих слов сразу в файл, без генерации всего массива в памяти
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    filename = "data.txt"
    with open(filename, "w") as file:
        count = 1
        for word in word_generator(alphabet):
            word_str = ''.join(word)
            if word_verification_1(word_str) and word_verification_2(word_str):
                file.write("{} - {}\n".format(str(count), word_str))
                print("{} - {} было записано в файл.".format(str(count), word_str))
                count += 1
                time.sleep(0.001)

def creating_data_for_work():
    create_data_file()

def finding_a_word_by_number(input_num):
    # поиск нужного слова по его номеру
    filename = "data.txt"
    with open(filename, "r") as file:
        for line in file:
            word_num, word = line.strip().split(" - ")
            if int(word_num) == input_num:
                return word
    print("Слова с таким номером нет.")

creating_data_for_work()
#num = int(input("Введите номер нужного слова: "))
#print(finding_a_word_by_number(num))
