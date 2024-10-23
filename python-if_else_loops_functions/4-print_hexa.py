#!/usr/bin/python3
# Author - Joseph Nishimwe

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for i in range(99):
    print("{} = 0x{}".format(i, hex(i)[2:]))
