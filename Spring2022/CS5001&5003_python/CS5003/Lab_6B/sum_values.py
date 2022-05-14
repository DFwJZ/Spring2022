"""
    CS5003 Spring 2022
    Lab 7. Problem 5
"""


def sum_values(ls, idx):
    if idx < len(ls) - 1:
        ls[idx] += sum_values(ls, idx + 1)
    return ls[idx]
