#!/usr/bin/python3
"""Adding all arguments to a Python list, and then savethem to a file"""


import sys
"""Imported sys"""

from os.path import exists
"""Imported exists"""

from 5-save_to_json_file import save_to_json_file
"""Imported save to json"""

from 6-load_from_json_file import load_from_json_file
"""Imported load from json"""


filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    item =[]

item.extend(sys.argv[1:])
save_to_json_file(items, filename)
