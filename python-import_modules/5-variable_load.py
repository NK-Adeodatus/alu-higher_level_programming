#!/usr/bin/python3
if __name__ == "__main__":
    import importlib

    # Load the module
    variable_load_5 = importlib.import_module('variable_load_5')

    # Print the value of the variable 'a'
    print(variable_load_5.a)
