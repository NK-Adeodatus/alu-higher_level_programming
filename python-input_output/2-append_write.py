#!/usr/bin/python3
"""
Writing a function to append a text at
the end of  a utf-8 file
"""


def append_write(filename="", text=""):
    """function to append a text on a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
