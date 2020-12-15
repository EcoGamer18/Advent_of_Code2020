"""def find_last_appear(lista, value):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == value:
            return i
    return -1"""
import time
from copy import deepcopy


def find_last_appear(lista, value):
    return lista[::-1].index(value) if value in lista else -1


def resolve2(lista,value):
    position = len(lista)
    seen=[[-1,-1] for x in range(value)]
    for i in lista:
        seen[i][0]=lista.index(i)
        seen[i][1]=1
    lista.extend([0 for x in range(value)])
    while position < value:
        if seen[lista[position-1]][1] > 0:
            lista[position] = position - 1 - seen[lista[position-1]][0]
            seen[lista[position - 1]][0] = position - 1
            seen[lista[position - 1]][1] += 1
        else:
            lista[position] = 0
            seen[lista[position - 1]][0] = position - 1
            seen[lista[position - 1]][1] =1
        #print(f"modified {position} = {lista[position]} ")
        position += 1
    """for i in lista:
        print(i,end=" ")"""
    return lista[value - 1],value -1


def read_file():
    with open("date_day_15.txt") as fp:
        lista = [int(x) for x in fp.read().split(",")]
    return lista


def main_day_15():
    lista = read_file()
    print(f"First puzzle: {resolve2(deepcopy(lista),2020)}")
    start = time.time()
    print(f"Second puzzle: {resolve2(deepcopy(lista),30000000)}")
    end = time.time()
    print("Second puzzle time",end - start)


main_day_15()
