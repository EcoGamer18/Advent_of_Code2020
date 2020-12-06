#second version

"""Useful websites:

https://stackoverflow.com/questions/6076270/lambda-function-in-list-comprehensions
https://stackoverflow.com/questions/1156087/search-in-lists-of-lists-by-given-index
https://www.geeksforgeeks.org/any-all-in-python/
https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
https://stackoverflow.com/questions/43158093/how-to-check-if-a-string-contains-only-lower-case-letters-and-numbers/43158132#43158132
https://stackoverflow.com/questions/43290202/python-typeerror-unhashable-type-slice-for-encoding-categorical-data
"""

def resolve_2(lista):
    verif = [{field[0]: field[1] for field in passport} for passport in lista if len(passport) == 8 or (
            len(passport) == 7 and any([passport[i][0] == 'cid' for i in range(7)]) is not True)]
    final = [1
             for passport in verif
             if 1920 <= int(passport["byr"]) <= 2002 and
             2010 <= int(passport["iyr"]) <= 2020 and
             2020 <= int(passport['eyr']) <= 2030 and
             (((True if 150 <= int(passport['hgt'][:passport['hgt'].find("cm")]) <= 193 else False) if passport['hgt'].find("cm") >= 0 else False) or
              ((True if 59 <= int(passport['hgt'][:passport['hgt'].find("in")]) <= 76 else False) if passport['hgt'].find("in") >= 0 else False)) and
             ((True if all(c.isdigit() or c.islower() for c in passport["hcl"][1:]) else False) if passport["hcl"][0] == "#" and len(passport["hcl"]) == 7 else False) and
             (True if passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False) and
             ((True if any(passport["pid"][i].isdigit() for i in
                           range(9)) else False) if len(passport["pid"]) == 9 else False)
             ]
    return sum(final)


def resolve_1(lista):
    return sum([1 for passport in lista if len(passport) == 8 or (
            len(passport) == 7 and any([passport[i][0] == 'cid' for i in range(7)]) is not True)])


def read_list():
    with open("Day_4\\date_day_4.txt", "r") as fp:
        lista = [list(j.split(":") for j in (i.replace("\n", " ")).split(" ")) for i in fp.read().split("\n\n")]
    return lista


def main_day_4():
    lista = read_list()
    print("First puzzle:")
    print(resolve_1(lista))
    print("Second puzzle:")
    print(resolve_2(lista))
