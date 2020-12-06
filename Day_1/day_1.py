# first puzzle advent of code

def problem1(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i]+list[j]==2020 :
                return list[i] * list[j]
    return -1


def problem2(list):
    for i in range(len(list) - 2):
        for j in range(i + 1, len(list) - 1):
            for k in range(j + 1, len(list)):
                if list[i] + list[j] + list[k] == 2020:
                    return list[i] * list[j] * list[k]
    return -1


def read_list():
    list = []
    with open("date_day_1.txt", "r") as fp:
        line = fp.readline()
        list.append(int(line))
        while line:
            list.append(int(line))
            line = fp.readline()
    return list


def main_day_1():
    lista = read_list()
    print(f"First problem:\n{problem1(lista)}")
    print(f"Second problem:\n{problem2(lista)}")

main_day_1()