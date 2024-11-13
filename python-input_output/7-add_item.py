#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file in JSON format.

The list is stored in a file named 'add_item.json'.
If the file does not exist, it will be created.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    # Load existing data from the file if it exists
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file does not exist, start with an empty list
    items = []

# Add new arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
