#!/usr/bin/python3
"""Adding all arguments to a Python list, and then savethem to a file"""


import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    item =[]

item.extend(sys.argv[1:])
save_to_json_file(items, filename)
