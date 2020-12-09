from Day_1.day_1_B import main_day_1
from Day_2.day_2_B import main_day_2
from Day_3.day_3_B import main_day_3
from Day_4.day_4_B import main_day_4
from Day_5.day_5_B import main_day_5
from Day_6.day_6_B import main_day_6
from Day_7.day_7 import main_day_7
from Day_8.day_8 import main_day_8
from Day_9.Day_9 import main_day_9


def console():
    print("Put 0 to close.")
    while True:
        dict={"1":main_day_1,"2":main_day_2,"3":main_day_3,"4":main_day_4,
              "5":main_day_5,"6":main_day_6,"7":main_day_7,"8":main_day_8,"9":main_day_9}
        option=input("Choose day:")
        if option in dict.keys():
            dict[option]()
        elif option =="0":
            break
        else:
            print("Does not exist.")

if __name__=="__main__":
    console()