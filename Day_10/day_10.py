"""
Diferentele sunt doar de 1 si 3.
Deci daca avem diferenta dintre 2 elem. egala cu 3, nu putem sa le aranja in vreun mod,dar
un sir de elemente cu diferenta de 1 poate avea mai multe moduri de aranjamente.

https://planetcalc.com/978/

# secventa de dif 1 de 2 elemente => 1 singur mod
(1,2)
# secventa de dif 1 de 3 elemente => 2 moduri
(1,2,3)
(1,3)
# secventa de dif 1 de 4 elemente => 4 moduri
(1,2,3,4)
(1,3,4)
(1,2,4)
(1,4)
2**(4-2)
# secventa de dif 1 de 5 elemente => 7 moduri
(1,2,3,4,5)
(1,2,3,5)
(1,2,4,5)
(1,3,4,5)
(1,2,5)
(1,3,5)
(1,4,5)
2**(5-2) -[(aranjamente de 3 luate cate 0)]
# secventa de dif 1 de 6 elemente => 13 moduri
(1,2,3,4,5,6)
(1,2,3,4,6)
(1,2,3,5,6)
(1,2,4,5,6)
(1,3,4,5,6)
(1,2,3,6)
(1,2,4,6)
(1,2,5,6)
(1,3,4,6)
(1,3,5,6)
(1,4,5,6)
(1,3,6)
(1,4,6)
2**(6-2) - [(aranjamente de 4 luate cate 1) - 2 + (aranjamente de 4 luate cate 0)]
"""


def resolve2(lista):
    moduri=[1,2,4,7,13,24]
    prod=1
    for i in lista:
        if len(i) > 2:
            prod *= moduri[len(i)-2]
    return prod


def modif_lista_for_2(lista):
    position = 0
    lista_modif = []
    while position < len(lista) - 1:
        i = position + 1
        while lista[i] - lista[i - 1] == 1 and i < len(lista)-1:
            i += 1
        lista_modif.append([x for x in lista[position:i]])
        position = i
    return lista_modif


def resolve1(lista):
    j1 = 1 if lista[0] == 1 else 3
    j3 = 1
    for i in range(len(lista) - 1):
        if lista[i + 1] - lista[i] == 1:
            j1 += 1
        elif lista[i + 1] - lista[i] == 3:
            j3 += 1
    return j1 * j3


def read_file():
    with open("date_day_10.txt") as fp:
        lista = [int(x) for x in fp.read().split("\n")]
    return sorted(lista)


def main_day_10():
    lista = read_file()
    """for i in lista:
        print(i)"""
    print(f"First puzzle: {resolve1(lista)}")
    listaa=[0]
    listaa.extend(lista)
    listaa.append(lista[-1]+3)
    #print(max(len(i) for i in modif_lista_for_2(listaa)))
    print(f"Second puzzle: {resolve2(modif_lista_for_2(listaa))}")


main_day_10()
