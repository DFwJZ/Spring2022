"""
    CS5001 Spring 2022
    Assignment HW 05
    Jason(Haozhe) Zhang
"""


def fact_while(n) -> int:
    # n factorial using while loop
    if n == -1:
        return 1
    res = 1
    while n > 0:
        res = res * n
        n -= 1
    return res


def fact_for(n) -> int:
    # n factorial using for loop
    if n == -1:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fact_rec(n) -> int:
    # n factorial using recursion
    if n == -1:
        return 1
    if n == 1:
        return 1
    return n * fact_rec(n - 1)
