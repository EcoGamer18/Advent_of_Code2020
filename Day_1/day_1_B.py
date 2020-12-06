# second version

"""Useful links:
https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
https://stackoverflow.com/questions/49761846/how-to-sum-two-numbers-in-a-list
https://www.codegrepper.com/code-examples/python/how+to+find+product+of+all+elements+in+list+python
https://www.geeksforgeeks.org/numpy-prod-python/
"""
import itertools
import numpy

def problem1(lista):
    for numbers in itertools.combinations(lista, 2):
        if sum(numbers) == 2020:
            return numpy.prod(numbers)
    return -1

def problem2(lista):
    for numbers in itertools.combinations(lista, 3):
        if sum(numbers) == 2020:
            return numpy.prod(numbers)
    return -1

def read_list():
    with open("Day_1\\date_day_1.txt", "r") as fp:
        lista = [int(i) for i in fp.read().split("\n")]
    return lista

def main_day_1():
    lista = read_list()
    lista = sorted(lista)
    print(f"First problem:\n{problem1(lista)}")
    print(f"Second problem:\n{problem2(lista)}")

