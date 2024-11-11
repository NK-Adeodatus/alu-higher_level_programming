#!/usr/bin/python3
"""
A script that adds all command-line arguments to a list and saves them 
to a file named `add_item.json`. If the file doesn't exist, it creates a new one.
Each time the script is run, new arguments are appended to the existing list in the file.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"

# Check if the file exists, load or create the list accordingly
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list with new arguments from the command line
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)

