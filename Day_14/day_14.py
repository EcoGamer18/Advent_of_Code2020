import itertools
from copy import deepcopy


def masking_2(mask, value):
    for i in range(36):
        if mask[i] in ["1", "X"]:
            value = value[:i] + mask[i] + value[i + 1:]
    return value


def floating_to_int(value):
    values=[]
    cartez = value.count("X")
    if cartez == 0:
        return bin_to_int(value)
    else:
        floating = list(itertools.product(["0", "1"], repeat=cartez))
        for x in floating:
            aux = deepcopy(value)
            pos = 0
            for i in range(36):
                if aux[i] == "X":
                    aux = aux[:i] + x[pos] + aux[i + 1:]
                    pos += 1
            aux = bin_to_int(aux)
            values.append(aux)
    return values


def resolve2(lista):
    final_sum = 0
    memo = {}
    for i in lista:
        for j in i[1:]:
            value_m = masking_2(i[0][0], dec_to_bin(int(j[0][4:-1])))
            for x in floating_to_int(value_m):
                memo[x] = int(j[1])
    return sum(memo[i] for i in memo.keys())


# -------------------------------------1----------------------------------------- #

def masking_1(mask, value):
    for i in range(36):
        if mask[i] in ["1", "0"]:
            value = value[:i] + mask[i] + value[i + 1:]
    return value


assert masking_1("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
                 "000000000000000000000000000000001011") \
       == "000000000000000000000000000001001001"


def resolve1(lista):
    final_sum = 0
    memo = [0] * (max([int(y[0][4:-1]) for i in lista for y in i[1:]]) + 2)
    for i in lista:
        for j in i[1:]:
            # print(i[0][0],dec_to_bin(int(j[1])),int(j[1]))
            value = masking_1(i[0][0], dec_to_bin(int(j[1])))
            memo[int(j[0][4:-1])] = bin_to_int(value)
            # print(f" mem[{int(j[0][4:-1])}] = {value}")
    final_sum += sum(memo)
    return final_sum


def bin_to_int(x):
    return int(x, 2)


assert bin_to_int("000000000000000000000000000000001011") == 11
assert bin_to_int("000000100101110000111101101101111111") == 633592703


def dec_to_bin(x):
    debris = ""
    for i in range(36 - len(str(bin(x)[2:]))):
        debris += "0"
    return debris + str(bin(x)[2:])


assert dec_to_bin(11) == "000000000000000000000000000000001011"
assert dec_to_bin(633592703) == "000000100101110000111101101101111111"


def read_file():
    with open("date_day_14.txt") as fp:
        lista = [
            [i.split(" = ") for i in [j for j in x.split("\n") if j != ""]]
            for x in fp.read().split("mask = ")[1:]
        ]
    return lista


def main_day_14():
    lista = read_file()
    """for i in lista:
        print(i)"""
    print(f"First puzzle: {resolve1(lista)}")
    print(f"Second puzzle: {resolve2(lista)}")


main_day_14()
