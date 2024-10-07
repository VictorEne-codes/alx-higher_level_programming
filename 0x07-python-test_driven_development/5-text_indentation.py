#!/usr/bin/python3
"""function to print lines"""


def text_indentation(text):
    """prints a text with 2 new lines after ? : .

    Args:
        text: input

    Return: texts

    Raises:
        TypeError: if ext is not a string
    """
    start = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            if i in ".?:":
                print("\n")
                print()
                start = True
            elif i == " " and start:
                continue
            else:
                print(i, end="")
                start = False

