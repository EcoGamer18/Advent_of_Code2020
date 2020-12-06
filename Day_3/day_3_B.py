# redone version
"""Useful websites:


"""

def resolve2(lista,right,down):
    position = right
    cnt_tree = 0
    scadent = len(lista[0])
    for i in range(down, len(lista),down):
        if position >= scadent:
            position -= scadent
        if lista[i][position] == "#":
            cnt_tree += 1
        position += right
    return cnt_tree

def read_lista():
    with open("Day_3\\date_day_3.txt", "r") as fp:
        lista = [i for i in fp.read().split("\n")]
    return lista

def main_day_3():
    lista=read_lista()
    print("First puzzle(with the lines):")
    print(resolve2(lista,3,1))
    print("Second puzzle final:")
    print(resolve2(lista,1,1)*resolve2(lista,3,1)*resolve2(lista,5,1)*
          resolve2(lista,7,1)*resolve2(lista,1,2))

