def resolve2(lista):
    position = 0
    while True:
        if lista[position][0] == "nop":
            a,b = resolve1([[lista[i][0],lista[i][1],0]  if i!=position else ["jmp",lista[i][1],0] for i in range(len(lista))])
            if b==0:
                return a
        elif lista[position][0] == "jmp":
            a, b = resolve1(
                [[lista[i][0], lista[i][1], 0] if i != position else ["nop", lista[i][1], 0] for i in range(len(lista))])
            if b == 0:
                return a
        position += 1
    
def resolve1(lista):
    position=0
    last_position=0
    accumulator=0
    while position<len(lista):
        if lista[position][2]==1:
            return accumulator,-1
        last_position = position
        if lista[position][0]=="nop":
            pass
        elif lista[position][0]=="acc":
            accumulator+=lista[position][1]
        elif lista[position][0]=="jmp":
            position+=lista[position][1]-1
        lista[position][2]+=1
        position += 1
    return accumulator,0

def read_list():
    with open("Day_8\\date_day_8.txt") as fp:
        lista=[i.split(" ") for i in fp.read().splitlines()]
        for i in lista:
            i[1]=int(i[1])
            i.append(0)
    return lista

def main_day_8():
    lista=read_list()
    """for i in lista:
        print(i)"""
    print("First puzzle:")
    print(resolve1(lista)[0])
    print("Second puzzle:")
    print(resolve2(lista))
