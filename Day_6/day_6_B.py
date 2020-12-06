#second version

"""
Useful links:
https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
https://www.geeksforgeeks.org/sets-in-python/
https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
https://stackoverflow.com/questions/30773911/union-of-multiple-sets-in-python
https://stackoverflow.com/questions/17666963/get-common-characters-from-strings
https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
"""

def resolve2(lista):
    sum = 0
    for group in lista:
        sum += len(set.intersection(*group))
    return sum

def resolve1(lista):
    sum = 0
    for group in lista:
        sum+=len(set.union(*group))
    return sum


def read_list():
    with open("Day_6\\date_day_6.txt") as f:
        lista =[list(i.split('\n')) for i in f.read().split("\n\n")]
        lista= [list(set(list(i)) for i in listuta) for listuta in lista]
    return lista


def main_day_6():
    lista = read_list()
    print("First puzzle: ")
    print(resolve1(lista))
    print("Second puzzle: ")
    print(resolve2(lista))


