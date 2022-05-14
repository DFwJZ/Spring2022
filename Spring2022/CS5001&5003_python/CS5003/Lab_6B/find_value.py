"""
    CS5003 Spring 2022
    Lab 7. Problem 8
"""


def find_value(ls, target):
    if len(ls) == 0:
        return False
    if ls[0] == target:
        return True
    return find_value(ls[1:], target)
