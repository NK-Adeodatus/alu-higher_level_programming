#!/usr/bin/python3
# Author - Joseph Nishimwe

for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        combination = "{}{}".format(digit1, digit2)
        if digit1 == 8 and digit2 == 9:
            print(combination)
        else:
            print(combination, end=", ")
