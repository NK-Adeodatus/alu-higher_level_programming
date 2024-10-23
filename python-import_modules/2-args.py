#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    number_of_args = len(argv) - 1

    if number_of_args == 0:
        print("0 arguments.")
    elif number_of_args == 1:
        print("1 argument:")
    else:
        print(f"{number_of_args} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
