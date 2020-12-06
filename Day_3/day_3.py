import simple_colors
def resolve1(lista):
    position=3
    cnt_tree=0
    scadent=len(lista[0])-1
    for i in range(1,len(lista)):
        if position<scadent:
            pass
        else:
            position-=scadent
        if lista[i][position] == "#":
            cnt_tree += 1
        #print(simple_colors.yellow(scadent,"bold"),simple_colors.red(position,"bold"),lista[i][:position]+simple_colors.red(lista[i][position],"bold")+lista[i][position+1:])
        position += 3
    return cnt_tree

def resolve2(lista,right,down):
    position = right
    cnt_tree = 0
    scadent = len(lista[0]) - 1
    for i in range(down, len(lista),down):
        if position < scadent:
            pass
        else:
            position -= scadent
        if lista[i][position] == "#":
            cnt_tree += 1
        """print(simple_colors.yellow(scadent, "bold"), simple_colors.red(position, "bold"),
              lista[i][:position] + simple_colors.red(lista[i][position], "bold") + lista[i][position + 1:])"""
        position += right
    return cnt_tree

def read_lista():
    lista = []
    with open("date_day_3.txt", "r") as fp:
        line = fp.readline()
        while line:
            lista.append(line)
            line = fp.readline()
    return lista

def main_day_3():
    lista=read_lista()
    print("First puzzle(with the lines):")
    print(resolve1(lista))
    print("Second puzzle tests:")
    print(resolve2(lista,1,1),resolve2(lista,3,1),resolve2(lista,5,1),
          resolve2(lista,7,1),resolve2(lista,1,2))
    print("Second puzzle final:")
    print(resolve2(lista,1,1)*resolve2(lista,3,1)*resolve2(lista,5,1)*
          resolve2(lista,7,1)*resolve2(lista,1,2))
