def sum_of_set(lista,result):
    for i in lista[:-2]:
        for j in lista[lista.index(i)+2:]:
            if sum(lista[lista.index(i):lista.index(j)])==result:
                return lista.index(i),lista.index(j)-1
    return -1,-1


def sum_of_min_and_max(lista):
    return max(lista)+min(lista)

def resolve2(lista):
    for i in range(25,len(lista)):
        a,b=sum_of_2(lista[i-25:i],lista[i])
        if a ==-1 and b ==-1:
            c,d=sum_of_set(lista[:i],lista[i])
            return sum_of_min_and_max(lista[c:d+1])
    return -1


def sum_of_2(lista,result):
    for i in lista[:-1]:
        for j in lista[lista.index(i)+1:]:
            if i + j == result:
                #print(i,"+",j,"=",result)
                return i,j
    return -1,-1


def resolve1(lista):
    for i in range(25,len(lista)):
        a,b=sum_of_2(lista[i-25:i],lista[i])
        if a ==-1 and b ==-1:
            return lista[i]
    return -1

def read_file():
    with open("Day_9\\date_day_9.txt") as fp:
        lista = [int(x) for x in fp.read().split("\n")]
    return lista


def main_day_9():
    lista = read_file()
    """for i in lista:
        print(i)"""
    print("First puzzle:\n"+str(resolve1(lista)))
    print("Second puzzle:\n"+str(resolve2(lista)))


