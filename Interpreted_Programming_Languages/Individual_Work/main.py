
import itertools

base_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
             "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
             "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25}

def word_generator():
    # тут будут создаваться все слова, которые потом будем записывать в файл
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    array_of_all_words = [''.join(p) for p in itertools.permutations(alphabet, len(alphabet))]
    return array_of_all_words

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
    print(temp_table)
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

def create_data_file(array_of_all_words):
    # проверяем слова на уникальность, затем уникальные записываем в файл
    temp_array = []
    for i in range(len(array_of_all_words)):
        if word_verification_1(array_of_all_words[i]):
            if word_verification_2(array_of_all_words[i]):
                temp_array.append(array_of_all_words[i])
    filename = "data.txt"
    file = open(filename, "w")
    for i in range(len(temp_array)):
        file.write("{} - {}\n".format(str(i + 1), str(temp_array[i])))
    file.close()

def creating_data_for_work():
    array_of_all_wards = word_generator()
    create_data_file(array_of_all_wards)

def finding_a_word_by_number(input_num):
    filename = "data.txt"
    with open(filename, "r") as file:
        for line in file:
            word_num, word = line.split(" - ")
            if word_num == input_num:
                return word
            else:
                print("Слова с таким номером нет.")

#creating_data_for_work()
num = int(input("Введите номер нужного слова: "))
print(finding_a_word_by_number(num))
