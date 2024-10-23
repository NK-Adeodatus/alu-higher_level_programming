#!/usr/bin/python3
# Author - Joseph Nishimwe

for i in range(26):
    letter = chr(97 + i)
    if letter != 'q' and letter != 'e':
        print("{}".format(letter), end="")
