#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    # Use list comprehension to filter names and sort them
    names = sorted([
        name for name in dir(hidden_4)
        if not name.startswith('__')
    ])

    # Print each name on a new line
    for name in names:
        print(name)
