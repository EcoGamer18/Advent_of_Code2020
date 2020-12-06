def resolve_1(list):
    number_invalid = 0
    present_fields = []
    for row in list:
        if row in ['\n', "\r\n"]:
            if len(present_fields) == 8 or (len(present_fields) == 7 and "cid" not in present_fields):
                number_invalid += 1
                # print("Correct")
            present_fields = []
        fill_fields = row.split(" ")
        if fill_fields != ["\n"]:
            for i in fill_fields:
                obj = i.split(":")
                present_fields.append(obj[0])
        # print(present_fields)
    if len(present_fields) == 8 or (len(present_fields) == 7 and "cid" not in present_fields):
        # print("Correct")
        number_invalid += 1
    return number_invalid


def verif_byr(number):
    if 1920 <= int(number) <= 2002:
        return True
    return False


def verif_iyr(number):
    if 2010 <= int(number) <= 2020:
        return True
    return False


def verif_eyr(number):
    if 2020 <= int(number) <= 2030:
        return True
    return False


def verif_hgt(height):
    if height.find("cm") >= 0:
        if 150 <= int(height[:height.find("cm")]) <= 193:
            return True
        return False
    elif height.find("in") >= 0:
        if 59 <= int(height[:height.find("in")]) <= 76:
            return True
        return False
    return False

assert verif_hgt("190cm") == True
assert verif_hgt("60in") == True
assert verif_hgt("190") == False
assert verif_hgt("190in") == False



def verif_hcl(color):
    if color[0] != "#":
        return False
    if len(color) != 7:
        return False
    for i in color[1:]:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", 'b', 'c', 'd', 'e', 'f']:
            return False
    return True


assert verif_hcl("#123abc") == True
assert verif_hcl("#b6652a") == True
assert verif_hcl("123abc") == False
assert verif_hcl("#123abz") == False


def verif_ecl(color_eye):
    # amb blu brn gry grn hzl oth
    if color_eye not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    return True


assert verif_ecl("wat") == False


def verif_pid(id_passport):
    if len(id_passport) != 9:
        return False
    for i in id_passport:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True


assert verif_pid("0123456789") == False
assert verif_pid("158898193") == True
assert verif_pid("000000001") == True


def verif_cid(id_country):
    return True


def resolve_2(list):
    number_invalid = 0
    present_fields = []
    valid_pass = True
    for row in list:
        if row in ['\n', "\r\n"]:
            if valid_pass == True:
                if len(present_fields) == 8 or (len(present_fields) == 7 and "cid" not in present_fields):
                    number_invalid += 1
                    #print("Correct")
            present_fields = []
            valid_pass = True
        fill_fields = row.split(" ")
        if fill_fields != ["\n"]:
            for count,i in enumerate(fill_fields):
                obj = i.split(":")
                present_fields.append(obj[0])
                if count == len(fill_fields)-1:
                    obj[1]=obj[1][:-1]
                dict = {"byr": verif_byr, "iyr": verif_iyr, "eyr": verif_eyr, "hgt": verif_hgt,
                        "hcl": verif_hcl, "ecl": verif_ecl, "pid": verif_pid, "cid": verif_cid}
                if dict[obj[0]](obj[1]) == False:
                    #print(obj[0],"is invalid.",obj[1])
                    valid_pass = False
        #print(present_fields)
    if valid_pass == True:
        if len(present_fields) == 8 or (len(present_fields) == 7 and "cid" not in present_fields):
            number_invalid += 1
            #print("Correct")
    return number_invalid


def read_list():
    list = []
    with open("date_day_4.txt", "r") as fp:
        line = fp.readline()
        while line:
            list.append(line)
            line = fp.readline()
    return list


def main_day_4():
    list = read_list()
    print("First puzzle:")
    print(resolve_1(list))
    print("Second puzzle:")
    print(resolve_2(list))

