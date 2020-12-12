def degrees_left(facing, degrees):
    directions = "NWSENWS"
    if degrees == 90:
        return directions[directions.find(facing) + 1]
    elif degrees == 180:
        return directions[directions.find(facing) + 2]
    elif degrees == 270:
        return directions[directions.find(facing) + 3]


def degrees_right(facing, degrees):
    directions = "NESWNES"
    if degrees == 90:
        return directions[directions.find(facing) + 1]
    elif degrees == 180:
        return directions[directions.find(facing) + 2]
    elif degrees == 270:
        return directions[directions.find(facing) + 3]


def resolve1(lista):
    east = 0
    north = 0
    facing = "E"
    for i in lista:
        if i[0] == "E":
            east += i[1]
        elif i[0] == "W":
            east -= i[1]
        elif i[0] == "N":
            north += i[1]
        elif i[0] == "S":
            north -= i[1]
        elif i[0] == "L":
            facing = degrees_left(facing, i[1])
        elif i[0] == "R":
            facing = degrees_right(facing, i[1])
        elif i[0] == "F":
            if facing == "E":
                east += i[1]
            elif facing == "W":
                east -= i[1]
            elif facing == "N":
                north += i[1]
            elif facing == "S":
                north -= i[1]
    return abs(east) + abs(north)


def degrees_leftW(facing, degrees, east, north):
    directions = "NWSENWS"
    if degrees == 90:
        return directions[directions.find(facing) + 1], -north, east
    elif degrees == 180:
        return directions[directions.find(facing) + 2], -east, -north
    elif degrees == 270:
        return directions[directions.find(facing) + 3], north, -east


def degrees_rightW(facing, degrees, east, north):
    directions = "NESWNES"
    if degrees == 90:
        return directions[directions.find(facing) + 1], north, -east
    elif degrees == 180:
        return directions[directions.find(facing) + 2], -east, -north
    elif degrees == 270:
        return directions[directions.find(facing) + 3], -north, east


def resolve2(lista):
    eastS = 0
    northS = 0
    eastW = 10
    northW = 1
    facing = "E"
    for i in lista:
        if i[0] == "E":
            eastW += i[1]
        elif i[0] == "W":
            eastW -= i[1]
        elif i[0] == "N":
            northW += i[1]
        elif i[0] == "S":
            northW -= i[1]
        elif i[0] == "L":
            facing, eastW, northW = degrees_leftW(facing, i[1], eastW, northW)
        elif i[0] == "R":
            facing, eastW, northW = degrees_rightW(facing, i[1], eastW, northW)
        elif i[0] == "F":
            eastS += i[1] * eastW
            northS += i[1] * northW
        # print(i,eastS,northS,eastW,northW)
    return abs(eastS), abs(northS), abs(eastS) + abs(northS)


def read_list():
    with open("date_day_12.txt") as fp:
        lista = [(x[0], int(x[1:])) for x in fp.read().split("\n")]
    return lista


def main_day_12():
    lista = read_list()
    print(f"First puzzle: {resolve1(lista)}")
    print(f"Second puzzle: {resolve2(lista)[2]}")


main_day_12()
