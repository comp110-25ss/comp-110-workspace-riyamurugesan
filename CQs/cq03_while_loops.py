"""Using a while loop to iterate over a string!"""

__author__: str = "730766142"


def num_instances(phrase: str, search_char: str) -> None:
    """Returns how many times a character appears in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    print(count)
