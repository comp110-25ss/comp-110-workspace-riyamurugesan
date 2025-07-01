"""Challenge Question: Recursion"""

__author__ = "730766142"


def f(n: int, k: int) -> int:
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
    # reached this solution by comparing f(2,k) & f(3,k) -using standard def. of the fn.
    # f(2,k) = 2k and f(3,k) = 3k; to get from 2k to 3k you have to add k
    # (which is the same for any two function calls where n is two consecutive numbers)
    # thus f(n-1,k) + k is equal to f(n,k)!
