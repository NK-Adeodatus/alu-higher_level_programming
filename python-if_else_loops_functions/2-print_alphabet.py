#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for i in range(26):
    print("{}".format(chr(97 + i)), end="")
