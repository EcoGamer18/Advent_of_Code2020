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
    return lista"""


def read_file():
    with open("date_day_7.txt","r") as fp:
        lista = [x.split(" bags contain ")[0].split(", ")
                for x in fp.read().split(".\n")
            ]
    return lista[:-1]


def main_day_7():
    lista = read_file()
    for i in lista:
        print(i)
    #print(resolve1(lista))


main_day_7()
