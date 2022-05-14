"""
    CS5003 Spring 2022
    Lab 7. Problem 4
"""


def lower_triangle(x):
    if x > 1:
        lower_triangle(x - 1)
    print(x * '*')
