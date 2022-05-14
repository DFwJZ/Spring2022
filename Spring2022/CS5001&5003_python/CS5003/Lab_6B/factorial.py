"""
    CS5003 Spring 2022
    Lab 7. Problem 2
"""


def factorial(x):
    if x <= 0:
        return 1
    return x * factorial(x - 1)
