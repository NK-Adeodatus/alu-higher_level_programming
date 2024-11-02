#!/usr/bin/python3
"""class mylist that inherits from lists"""


class MyList(list):
    """subclass that inherits from list"""

    def print_sorted(self):
        """print list in ascending order"""
        print(sorted(self))
