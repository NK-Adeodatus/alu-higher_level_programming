#!/usr/bin/python3


def print_last_digit(number):
    """Function to print the last digit of a number."""
    last_digit = abs(number) % 10  # Get the last digit
    print(last_digit, end='')        # Print the last digit without a newline
    return last_digit                 # Return the last digit
