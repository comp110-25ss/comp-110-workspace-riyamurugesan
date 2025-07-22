"""Writing the find_and_remove_max function."""

__author__: str = "730766142"


def find_and_remove_max(values: list[int]) -> int:
    if len(values) == 0:
        return -1
    i: int = 0
    max: int = values[0]
    while i < len(values):
        if values[i] > max:
            max = values[i]
        i += 1
    i = 0
    while i < len(values):
        if values[i] == max:
            values.pop(i)
            i -= 1
        i += 1
    return max
