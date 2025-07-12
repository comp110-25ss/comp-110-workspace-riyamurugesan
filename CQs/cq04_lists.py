"""Mutating functions."""

__author__: str = "730766142"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list: list[int], number: int) -> None:
    """Appends the new number to the end of the list."""
    list.append(number)


def double(list: list[int]) -> None:
    """Multiplies every element in the list by 2."""
    i: int = 0  # index value
    while i < len(list):
        list[i] *= 2
        i += 1


double(list_2)
print(list_1)
print(list_2)  # both list 1 and list 2 will be the same - [2,4,6]
# because they were set equal to one another
# any change to one list will be reflected in the other
