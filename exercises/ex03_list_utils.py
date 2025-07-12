"""List Utility Functions Exercise"""

__author__: str = "730766142"


def all(list: list[int], number: int) -> bool:
    """Checks whether every element of the list is the same as the given number"""
    i: int = 0
    if len(list) == 0:  # adding this line so that an empty set will return False
        # only non-empty sets will proceed to line 12 (while loop)
        return False
    while i < len(list):
        if list[i] == number:
            i += 1
        else:
            return False
    return True  # returning outside of loop so it'll run only when condition is False


def max(list: list[int]) -> int:
    """Returns the largest number in the list"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1  # starting at 1 b/c with i=0, I used list[i+1] which gave an IndexError
    largest_number: int = list[
        0
    ]  # stating the max is the first element and comparing to subsequent elements
    while i < len(list):
        if largest_number >= list[i]:
            i += 1
        else:
            largest_number = list[
                i
            ]  # replacing largest number with the higher # out of the two.
            i += 1
    return largest_number


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks if all elements are equal between two lists"""
    i: int = 0
    while i < len(first_list) or i < len(
        second_list
    ):  # had to add the or statement so that fxn would work if there was one empty set
        # it allows the condition to be True & the code inside while loop will execute
        # if condition=False, then the fxn would incorrectly return True
        if len(first_list) != len(
            second_list
        ):  # have to do this first so there is not an IndexError when comparing lists
            return False
        elif first_list[i] == second_list[i]:
            i += 1
        else:
            return False
    return (
        True  # returning outside of loop so it'll run after going through entire list
    )


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Mutating First List by Appending Second List's Values"""
    i: int = 0
    while i < len(
        second_list
    ):  # need to use a while loop to append EACH element of list 2
        first_list.append(second_list[i])
        i += 1
