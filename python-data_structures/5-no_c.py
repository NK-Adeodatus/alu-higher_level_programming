def no_c(my_string):
    """Remove all characters 'c' and 'C' from the string.

    The function should return the new string.
    You are not allowed to import any module.
    You are not allowed to use str.replace().
    """
    new_str = ""

    for char in my_string:
        if char not in ('c', 'C'):
            new_str += char

    return new_str
