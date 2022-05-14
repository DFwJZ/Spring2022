"""
    CS5003 Spring 2022
    Lab 7. Problem 3
"""


def upper_triangle(x):
    print(x * '*')
    if x == 1:
        return
    return upper_triangle(x - 1)
