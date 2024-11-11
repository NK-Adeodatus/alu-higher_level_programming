#!/usr/bin/python3
"""Code to write a string to file"""


def write_file(filename="", text=""):
    """ function to write a string to a file(utf-8)"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
