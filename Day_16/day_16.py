from collections import Counter


def num_in_rules(rules, value):
    for i in rules:
        for j in range(len(i[1])):
            if i[1][j][0] <= value <= i[1][j][1]:
                return True
    return False


def resolve1(rules, n_ticket):
    error_rate = 0
    for i in n_ticket:
        for j in i:
            if num_in_rules(rules, j) is False:
                error_rate += j
    return error_rate


def num_in_rules_2(rules, value):
    sir = []
    for i in rules:
        for j in range(len(i[1])):
            if i[1][j][0] <= value <= i[1][j][1]:
                sir.append(i[0])
                break
    return sir


def resolve2(rules, y_ticket, n_ticket):
    dict = {}
    for i in n_ticket:
        for j in range(len(i)):
            aux = num_in_rules_2(rules, i[j])
            if aux == []:
                n_ticket = [x for x in n_ticket if x != i]
    for i in n_ticket:
        for j in range(len(i)):
            aux = num_in_rules_2(rules, i[j])
            for x in aux:
                if x in dict.keys():
                    dict[x].append(j)
                else:
                    dict[x] = [j]
    for x in dict.keys():
        dict[x] = [[i, j] for i, j in Counter(dict[x]).items() if j == len(n_ticket)]
    dict = {x: y for x, y in sorted(dict.items(), key=lambda item: len(item[1]))}
    final_positions = [""] * len(n_ticket[0])
    for x in dict.keys():
        for j in dict[x]:
            if final_positions[j[0]] == "":
                final_positions[j[0]] = x
                break
    product = 1
    for i in range(len(y_ticket)):
        if final_positions[i].find("departure") > -1:
            product *= y_ticket[i]
    return product


def read_File():
    with open("date_day_16.txt") as fp:
        lista = [x.split("\n") for x in fp.read().split("\n\n")]
        for i in range(len(lista[0])):
            lista[0][i] = lista[0][i].split(": ")
            lista[0][i][1] = lista[0][i][1].split(" or ")
            for x in range(len(lista[0][i][1])):
                lista[0][i][1][x] = [int(y) for y in lista[0][i][1][x].split("-")]
        rules = lista[0]
        y_ticket = [int(x) for x in lista[1][1].split(",")]
        for i in range(1, len(lista[2])):
            lista[2][i] = [int(x) for x in lista[2][i].split(",")]
        n_ticket = lista[2][1:]
    return rules, y_ticket, n_ticket


def main_day_16():
    rules, y_ticket, n_ticket = read_File()
    """for i in rules:
        print(i)
    print(y_ticket)
    for i in n_ticket:
        print(i)"""
    print(f"First puzzle: {resolve1(rules,n_ticket)}")
    print(f"Second puzzle: {resolve2(rules, y_ticket, n_ticket)}")


main_day_16()
