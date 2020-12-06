#second version

"""Useful websites:
https://realpython.com/list-comprehension-python/
https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python


"""

def verify2(lista):
    return sum([ 1
                 if (linie[2][int(linie[0][0])-1] == linie[1][0] and not linie[2][int(linie[0][1])-1] == linie[1][0]) or (not linie[2][int(linie[0][0])-1] == linie[1][0] and linie[2][int(linie[0][1])-1] == linie[1][0])
                 else 0
                 for linie in lista])

def verify1(lista):
    return len(lista)-sum(
        [0
         if int(linie[0][0]) <= sum([1 for carac in range(len(linie[2]))if linie[2][carac] == linie[1][0]]) <= int(linie[0][1])
         else 1
         for linie in lista
         ]
    )


def read_list():
    with open("Day_2\\date_day_2.txt", "r") as fp:
        lista = [[ x[0].split("-") , x[1][0] , x[2] ] for x in(i.split(" ") for i in fp.read().split("\n"))]
    return lista

def main_day_2():
    lista=read_list()
    print("First puzzle:")
    print(verify1(lista))
    print("Second puzzle:")
    print(verify2(lista))

