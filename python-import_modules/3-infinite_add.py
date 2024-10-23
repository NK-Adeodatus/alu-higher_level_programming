#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    # Use map to convert arguments to integers and sum them up
    total_sum = sum(map(int, argv[1:]))

    # Print the result
    print(total_sum)
