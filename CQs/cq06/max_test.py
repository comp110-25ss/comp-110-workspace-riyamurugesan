"""Testing the find_and_remove_max function for use and edge cases."""

__author__: str = "730766142"

from CQs.cq06.find_max import find_and_remove_max


def test_find_and_remove_max_return_val_use_case() -> None:
    """Testing if find_and_remove_max returns the expected value for a use case"""
    assert find_and_remove_max([3, 5, 7, 2, 7]) == 7


def test_find_and_remove_max_mutate_input_use_case() -> None:
    """Testing if find_and_remove_max mutates the input predictably for a use case"""
    a: list[int] = [2, 5, 5, 3, 4]
    find_and_remove_max(a)
    assert a == [2, 3, 4]


def test_find_and_remove_max_return_val_edge_case() -> None:
    """Testing if find_and_remove_max returns the expected value for an edge case"""
    assert find_and_remove_max([]) == -1
