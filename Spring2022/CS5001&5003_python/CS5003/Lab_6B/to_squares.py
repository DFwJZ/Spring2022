"""
    CS5003 Spring 2022
    Lab 7. Problem 6
"""


def to_squares(ls, idx):
    if idx <= len(ls) - 1 and idx >= 0:
        ls[idx] = ls[idx] ** 2
        to_squares(ls, idx + 1)
    return ls
