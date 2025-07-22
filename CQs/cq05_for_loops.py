"""Practice for-looping over lists and dicts."""

__author__: str = "730766142"


def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum


def get_keys(dictionary: dict[str, int]) -> list[str]:
    list_of_keys: list[str] = []
    for key in dictionary:
        list_of_keys.append(key)
    return list_of_keys


def get_values(dictionary: dict[str, int]) -> list[int]:
    list_of_values: list[int] = []
    for key in dictionary:
        list_of_values.append(dictionary[key])
    return list_of_values
