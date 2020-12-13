import re

from functools import reduce
"""Useful links:
https://brilliant.org/wiki/chinese-remainder-theorem/
https://www.dcode.fr/chinese-remainder
http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
https://www.youtube.com/watch?v=ru7mWZJlRQg
https://github.com/bluhb/AdventOfCode2020/blob/master/day11/main.py
"""
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def resolve2_2(lista):
    dict = [[int(x), int(x)-i] for i, x in enumerate(lista[1]) if x != "x"]
    return chinese_remainder([x[0] for x in dict], [x[1] for x in dict])


def verify(dict, number):
    for i in dict:
        if (number + i[1]) % int(i[0]) != 0:
            return False
    return True


def resolve2_1(lista):
    time = 100005000000000
    dict = [[x, i] for i, x in enumerate(lista[1]) if x != "x"]
    time = (time // int(dict[0][0]) + 1) * int(dict[0][0])
    while verify(dict, time) == False:
        time += int(dict[0][0])
    return time


def resolve1(lista):
    time = lista[0][0]
    minim_dif = lista[0][0]
    minim_id = -1
    for i in lista[1]:
        if i != "x":
            number_id = int(i)
            number = (time // number_id + 1) * number_id
            # print(number_id,number-time)
            if number - time < minim_dif:
                minim_dif, minim_id = (number - time), number_id
    return minim_dif * minim_id


def read_file():
    with open("date_day_13.txt") as fp:
        lista = [i.split(",") for i in [x for x in fp.read().split("\n")]]
        lista[0][0] = int(lista[0][0])
    return lista


def main_day_13():
    lista = read_file()
    """for i in lista:
        print(i)"""
    print(f"First puzzle: {resolve1(lista)}")
    # print(resolve2_1(lista))
    print(f"Second puzzle: {resolve2_2(lista)}")


main_day_13()
