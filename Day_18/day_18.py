from copy import deepcopy
from functools import reduce


def suma(lista):
    try:
        first = lista.index("(")
    except ValueError:
        first = -1
    last = first + 1
    if first != -1:
        yours = 0
        while last < len(lista):
            if lista[last] == "(":
                yours += 1
            elif lista[last] == ")":
                if yours == 0:
                    break
                else:
                    yours -= 1
            last += 1
    sum = 0
    while first != -1 and last != len(lista):
        sum2 = suma(lista[first + 1:last])
        lista[first] = sum2
        del lista[first + 1:last + 1]

        try:
            first = lista.index("(")
        except ValueError:
            first = -1
        last = first + 1
        if first != -1:
            yours = 0
            while last < len(lista):
                if lista[last] == "(":
                    yours += 1
                elif lista[last] == ")":
                    if yours == 0:
                        break
                    else:
                        yours -= 1
                last += 1
    for i in lista:
        sum = lista[0]
        for i in range(1, len(lista), 2):
            if lista[i] == "+":
                sum += lista[i + 1]
            elif lista[i] == "*":
                sum *= lista[i + 1]
    return sum


def resolve1(lista):
    sum = 0
    for i in lista:
        sum += suma(i)
    return sum


def first_and_last(lista):
    try:
        first = lista.index("(")
    except ValueError:
        first = -1
    last = first + 1
    if first != -1:
        yours = 0
        while last < len(lista):
            if lista[last] == "(":
                yours += 1
            elif lista[last] == ")":
                if yours == 0:
                    break
                else:
                    yours -= 1
            last += 1
    return first, last


def first_sum(lista):
    try:
        first = lista.index("+")
    except:
        first = -1
    return first


def first_multi(lista):
    try:
        first = lista.index("*")
    except:
        first = -1
    return first


def suma2(lista):
    first, last = first_and_last(lista)
    while first != -1 and last != -1:
        sum1 = suma2(lista[first + 1:last])
        lista[first] = sum1
        del lista[first + 1:last + 1]
        first, last = first_and_last(lista)
    i = first_sum(lista)
    while i != -1:
        sum1 = lista[i - 1] + lista[i + 1]
        lista[i - 1] = sum1
        del lista[i:i + 2]
        i = first_sum(lista)
    i = first_multi(lista)
    while i != -1:
        sum1 = lista[i - 1] * lista[i + 1]
        lista[i - 1] = sum1
        del lista[i:i + 2]
        i = first_multi(lista)
    return lista[0]


def resolve2(lista):
    sum = 0
    for i in lista:
        sum += suma2(i)
    return sum


def read_file():
    with open("date_day_18.txt") as fp:
        lista = [[int(i) if i.isdigit() else i for i in x.replace(" ", "")] for x in fp.read().split("\n")]
    return lista


def main_day_18():
    lista = read_file()
    print(f"First puzzle: {resolve1(deepcopy(lista))}")
    print(f"Second puzzle: {resolve2(deepcopy(lista))}")


main_day_18()
