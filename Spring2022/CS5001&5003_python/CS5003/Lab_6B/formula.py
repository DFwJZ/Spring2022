"""
    CS5003 Spring 2022
    Lab 7. Problem 1
"""


def formula(x):
    if x <= 1:
        return 3
    return 2 * formula(x - 1) + 5
