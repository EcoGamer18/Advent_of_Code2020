#second puzzle advent of code

def verify2(lista):
    numar_parol=0
    for linie in lista:
        operatie=linie.split(" ")
        number_of_times=operatie[0].split("-")
        cnt=0
        if operatie[2][int(number_of_times[0])-1] == operatie[1][0]:
            cnt+=1
        if operatie[2][int(number_of_times[1])-1] == operatie[1][0]:
            cnt+=1
        if cnt==1:
            pass
        else:
            #print(operatie,cnt)
            numar_parol+=1
    return numar_parol

def verify1(lista):
    numar_parol=0
    for linie in lista:
        operatie=linie.split(" ")
        number_of_times=operatie[0].split("-")
        cnt=0
        for carac in range(len(operatie[2])-1):
            if operatie[2][carac] == operatie[1][0]:
                cnt+=1
        if int(number_of_times[0]) <= cnt <= int(number_of_times[1]):
            pass
        else:
            numar_parol+=1
    return numar_parol


def read_list():
    list = []
    with open("date_day_2.txt", "r") as fp:
        line = fp.readline()
        list.append(line)
        while line:
            list.append(line)
            line = fp.readline()
    return list

def main_day_2():
    list=read_list()
    print("First puzzle:")
    print(len(list)-1-verify1(list[1:]))
    print("Second puzzle:")
    print(len(list)-1-verify2(list[1:]))
