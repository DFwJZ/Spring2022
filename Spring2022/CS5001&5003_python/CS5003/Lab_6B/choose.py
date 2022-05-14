"""
    CS5003 Spring 2022
    Lab 7. Problem 10
"""


def choose(k, n):
    if k == 0 or k == n:
        return 1
    else:
        return choose(k - 1, n - 1) + choose(k, n - 1)
