"""#botched version

def find_index_bag(type_color, color, lista):
    return [[i,j]
            for i in range(len(lista))
            for j in range(1,len(lista[i]))
            if lista[i][j][1] == type_color and lista[i][j][2] == color
            ]


#bfs

def resolve1(lista):
    verificare = find_index_bag("shiny", "gold", lista)
    done =[[lista[x[0]][0][0],lista[x[0]][0][1]] for x in verificare]
    gold_len = len(verificare)
    suma=0
    for i in verificare:
        type_color = lista[i[0]][0][0]
        color= lista[i[0]][0][1]
        suma+=lista[i[0]][i[1]][0]
        verificare.extend([x
                           for x in find_index_bag(type_color,color,lista)
                           if [lista[x[0]][0][0],lista[x[0]][0][1]] not in done
                           ])
        done = [[lista[x[0]][0][0], lista[x[0]][0][1]] for x in verificare]
    return suma- sum([lista[i[0]][i[1]][0] for i in verificare[:gold_len]])


def read_file():
    with open("date_day_7.txt", "r") as fp:
        lista = [[x for x in i.split(",")] for i in fp.read().split(".\n")]
        for x in lista:
            aux = []
            x[0] = x[0].split(" contain ")
            aux.append(x[0][1].split(" ")[:-1])
            aux.extend(i.split(" ")[1:-1] for i in x[1:])
            x[0] = x[0][0].split(" ")[:-1]
            del x[1:]
            for i in aux:
                if i[0] == "no":
                    i[0] = 0
                    i[1] = ""
                else:
                    i[0] = int(i[0])
            x.extend(aux)
    return lista
"""

import simple_colors
"""Useful links:
https://careerkarma.com/blog/python-print-without-new-line/
https://stackoverflow.com/questions/46878699/all-prints-in-function-with-tabs-python
https://www.geeksforgeeks.org/python-product-of-elements-using-index-list/
https://www.geeksforgeeks.org/queue-in-python/
https://www.geeksforgeeks.org/union-function-python/
https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
https://stackoverflow.com/questions/37372603/how-to-remove-specific-substrings-from-a-set-of-strings-in-python
https://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python
https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41
"""

def find_bags_1(bag, lista):
    return [
        [j[0], i[0]]
        for i in lista
        for j in i[1:]
        if len(bag.intersection(j[1])) == 2
    ]


def find_bags_2(bag, lista):
    for i in lista:
        if len(bag.intersection(i[0])) == 2:
            return lista.index(i)


# 41559
def resolve2(lista, setb={"shiny", "gold"}, tabs="\t"):
    color = find_bags_2(setb, lista)
    prod = 0
    print(str(lista[color][0]))
    for i in lista[color][1:]:
        if i[0] != 0:
            print(tabs + str(i[0]) + " ", end="")
            x=resolve2(lista, i[1], tabs + "\t")
            prod += i[0] * (x+1 if x!=1 else 1)
    return prod if prod != 0 else 1


def resolve1(lista):
    queue = find_bags_1({"shiny", "gold"}, lista)
    for i in queue:
        queue.extend([i for i in find_bags_1(i[1], lista) if i[1] not in [x[1] for x in queue]])
    return len(queue)


def read_file():
    with open("Day_7\\date_day_7.txt", "r") as fp:
        lista = [x.split(" bags contain ")
                 for x in fp.read().split(".\n")
                 ]
        for i in lista:
            i[0] = set(i[0].split(" "))
            i[1] = [
                [
                    int(x.split(" ")[0] if x.split(" ")[0] != "no" else 0), set(x.split(" ")[1:-1])
                ]
                for x in i[1].split(", ")
            ]
            i[1:len(i[1]) + 1] = i[1]
    return lista


def main_day_7():
    lista = read_file()
    """for i in lista:
        print(i)"""
    print("First puzzle:")
    print(resolve1(lista))
    print("Second puzzle:")
    print(resolve2(lista))
