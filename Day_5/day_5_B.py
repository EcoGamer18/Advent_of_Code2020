#second version
# to revise : how to make divide et impera with easier and faster means
"""
useful links:
https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
https://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops
https://thepythonguru.com/python-builtin-functions/max/
"""
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


def resolve1(lista):
    return max([find_column(pass_id[0]) * 8 + find_row(pass_id[1]) for pass_id in lista])


def resolve2(lista):
    max_pass_id=resolve1(lista)
    frec = [i for i in range(max_pass_id)
            if i not in [find_column(pass_id[0]) * 8 + find_row(pass_id[1])  for pass_id in lista]]
    response = [frec[i] for i in range(1, len(frec)-1) if frec[i] - frec[i - 1] != 1 and frec[i + 1] - frec[i] != 1]
    if response == []:
        return frec[-1]
    return response[0]

def read_list():
    with open("Day_5\\date_day_5.txt") as f:
        lista = [[i[:7], i[7:]] for i in f.read().split("\n")]
    return lista


def main_day_5():
    lista = read_list()
    print("First puzzle: ")
    print(resolve1(lista))
    start = time.time()
    print("Second puzzle:")
    print(resolve2(lista))
    end = time.time()
    print("Second task took",end-start,"seconds.")
