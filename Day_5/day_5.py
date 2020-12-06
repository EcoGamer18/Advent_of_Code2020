# first version(have to have a \n at the end of the txt)
import time


def find_row(row, bottom=0, top=7):
    if len(row) == 1:
        if row[0] == "L":
            return bottom
        elif row[0] == "R":
            return top
    medium = (top + bottom) // 2
    if row[0] == "R":
        return find_row(row[1:], medium + 1, top)
    elif row[0] == "L":
        return find_row(row[1:], bottom, medium)
    return -1


def find_column(column, bottom=0, top=127):
    if len(column) == 1:
        if column[0] == "F":
            return bottom
        elif column[0] == "B":
            return top
    medium = (top + bottom) // 2
    if column[0] == "B":
        return find_column(column[1:], medium + 1, top)
    elif column[0] == "F":
        return find_column(column[1:], bottom, medium)
    return -1


def resolve1(list):
    max_id = -1
    for pass_id in list:
        column = find_column(pass_id[:7])
        row = find_row(pass_id[7:10])
        if column * 8 + row > max_id:
            max_id = column * 8 + row
        """print(simple_colors.red("Pass:", 'italic') + pass_id)
        print(simple_colors.yellow("Column:", 'italic'), column)
        print(simple_colors.yellow("Row:", 'italic'), row)
        print(simple_colors.blue("ID:", 'bold'), column * 8 + row)
        print("----------------------------")"""
    return max_id


def resolve2(list):
    max_id = -1
    lista = [0 for i in range(127 * 8 + 8)]
    for pass_id in list:
        column = find_column(pass_id[:7])
        row = find_row(pass_id[7:10])
        lista[column * 8 + row] = 1
        if column * 8 + row > max_id:
            max_id = column * 8 + row
        """print(simple_colors.red("Pass:", 'italic') + pass_id)
        print(simple_colors.yellow("Column:", 'italic'), column)
        print(simple_colors.yellow("Row:", 'italic'), row
        print(simple_colors.blue("ID:", 'bold'), column * 8 + row)
        print("----------------------------")"""
    free_spots = []
    for i in range(max_id + 1):
        if lista[i] == 0:
            free_spots.append(i)

    for i in range(1, len(free_spots) - 1):
        if free_spots[i - 1] != free_spots[i] - 1 and free_spots[i + 1] != free_spots[i] + 1:
            return free_spots[i]

    return free_spots[-1]


def read_list():
    list = []
    with open("date_day_5.txt", "r") as fp:
        line = fp.readline()
        while line:
            list.append(line)
            line = fp.readline()
    return list

def main_day_5():
    lista = read_list()
    print("First puzzle: ")
    print(resolve1(lista))
    start = time.time()
    print("Second puzzle:")
    print(resolve2(lista))
    end = time.time()
    print("Second task took",end-start,"seconds.")
