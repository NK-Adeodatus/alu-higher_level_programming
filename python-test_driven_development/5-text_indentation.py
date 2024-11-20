#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    these characters: ., ?, :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    special_chars = {".", "?", ":"}
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1
            # Skip any extra spaces after the special character
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
