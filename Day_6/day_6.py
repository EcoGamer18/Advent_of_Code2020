import simple_colors

# botched version

import simple_colors


def resolve2(lista, printare=0):
    frec = []
    sum = 0
    first = 1
    for row in lista:
        if row == '\n':
            sum += len(frec)
            if printare == 0:
                print(simple_colors.red("Questions: ", "bold"), frec)
                print(simple_colors.yellow("Sum now: ", "bold"), sum)
                print("------------------------------")
            frec = []
            first = 1
        else:
            if first == 0:
                frec=[char for char in frec if row.find(char)!=-1]
            else:
                frec=[char for char in row if char!="\n"]
                first = 0
    sum += len(frec)
    return sum


assert resolve2(["abcd", 'abc', 'bc', '\n'], 1) == 2
assert resolve2(["cdf", 'abcdef', 'bcef', '\n'], 1) == 2
assert resolve2(["cdf", 'ab', 'bcef', '\n'], 1) == 0
assert resolve2(["abc\n", '\n', 'a\n', 'b\n', 'c\n', '\n', 'ab\n', 'ac\n', '\n',
                 'a\n','a\n','a\n','\n','b\n','\n',], 1) == 6


def resolve1(lista, printare=0):
    frec = []
    sum = 0
    for row in lista:
        if row == '\n':
            sum += len(frec)
            frec = []
        else:
            for char in row:
                if char not in frec and char != "\n":
                    frec.append(char)
        if printare == 0:
            print(simple_colors.yellow("Sum now: ", "bold"), sum)
            print(simple_colors.red("Frec now: ", "bold"), frec)
    sum += len(frec)
    return sum


def read_list():
    list = []
    with open("date_day_6.txt", "r") as fp:
        line = fp.readline()
        while line:
            list.append(line)
            line = fp.readline()
    return list


def main_day_6():
    lista = read_list()
    print("First puzzle: ")
    print(resolve1(lista, 1))
    print("Second puzzle: ")
    print(resolve2(lista,1))

