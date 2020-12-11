from copy import deepcopy
from itertools import starmap, product
import sys

sys.setrecursionlimit(5000)


def empty1(x, y, lista):
    cells = [lista[i[0]][i[1]]
             for i in starmap(lambda a, b: (x + a, y + b), product((0, -1, +1), (0, -1, +1)))
             if 0 <= i[0] < len(lista) and 0 <= i[1] < len(lista[0]) and i != (x, y)]
    if "#" in cells:
        return False
    return True


def occupied1(x, y, lista):
    cells = [lista[i[0]][i[1]]
             for i in starmap(lambda a, b: (x + a, y + b), product((0, -1, +1), (0, -1, +1)))
             if 0 <= i[0] < len(lista) and 0 <= i[1] < len(lista[0]) and i != (x, y)]
    if sum([1 for x in cells if x == "#"]) >= 4:
        return True
    return False


def matrici_egale(listaa, lista):
    for i in range(len(listaa)):
        for j in range(len(listaa[i])):
            if listaa[i][j] != lista[i][j]:
                return False
    return True


def rules1(lista):
    listaa = deepcopy(lista)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == "L":
                if empty1(i, j, lista) is True:
                    listaa[i][j] = "#"
            elif lista[i][j] == "#":
                if occupied1(i, j, lista) is True:
                    listaa[i][j] = "L"
    print("reguli aplicate")
    if matrici_egale(listaa, lista) is False:
        return rules1(listaa)
    else:
        return sum([1 for x in listaa for c in x if c == "#"])


def empty2(x, y, lista):
    cells = []
    positions = [[0, 1], [0, -1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1]]
    circle = 1
    while len(cells) < 8 and any(True
                                 for i in range(len(positions))
                                 if 0 <= x+circle * positions[i][0] < len(lista) and 0 <= y+circle * positions[i][1] < len(lista[0])) == True:
        position_elim = []
        for i in range(len(positions)):
            if 0 <= x+circle * positions[i][0] < len(lista) and 0 <= y+circle * positions[i][1] < len(lista[0]):
                if lista[x+circle * positions[i][0]][y+circle * positions[i][1]] != ".":
                    cells.append([x+circle * positions[i][0], y+circle * positions[i][1]])
                    position_elim.append(positions[i])
        positions=[j for j in positions if j not in position_elim]
        circle += 1
    if "#" in [lista[i[0]][i[1]] for i in cells]:
        return False
    return True


def occupied2(x,y,lista):
    cells = []
    positions = [[0, 1], [0, -1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1]]
    circle = 1
    while len(cells) < 8 and any(True
                                 for i in range(len(positions))
                                 if 0 <= x + circle * positions[i][0] < len(lista) and 0 <= y + circle * positions[i][
        1] < len(lista[0])) == True:
        position_elim = []
        for i in range(len(positions)):
            if 0 <= x + circle * positions[i][0] < len(lista) and 0 <= y + circle * positions[i][1] < len(lista[0]):
                if lista[x + circle * positions[i][0]][y + circle * positions[i][1]] != ".":
                    cells.append([x + circle * positions[i][0], y + circle * positions[i][1]])
                    position_elim.append(positions[i])
        positions = [j for j in positions if j not in position_elim]
        circle += 1
    if sum([1 for i in cells if lista[i[0]][i[1]]=="#"])>=5:
        return True
    return False

def rules2(lista):
    listaa = deepcopy(lista)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == "L":
                if empty2(i, j, lista) is True:
                    listaa[i][j] = "#"
            elif lista[i][j] == "#":
                if occupied2(i, j, lista) is True:
                    listaa[i][j] = "L"
    print("reguli aplicate")
    if matrici_egale(listaa, lista) is False:
        return rules2(listaa)
    else:
        return sum([1 for x in listaa for c in x if c == "#"])

def read_file():
    with open("date_day_11.txt") as fp:
        lista = [[c for c in x] for x in fp.read().split("\n")]
    return lista


def main_day_11():
    lista = read_file()
    print(rules2(lista))


main_day_11()
