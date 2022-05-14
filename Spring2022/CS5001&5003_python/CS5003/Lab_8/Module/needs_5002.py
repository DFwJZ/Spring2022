"""
    CS5003 Spring 2022
    Assignment Lab 8 Module 11
    Jason(Haozhe) Zhang and Manu Singh and Yuan wang
"""


def needs_5002(x, y):
    if isinstance(x, list):
        raise AttributeError
    if isinstance(y, list):
        raise AttributeError
    return list(x - y)
