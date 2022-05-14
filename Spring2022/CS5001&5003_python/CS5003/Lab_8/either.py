"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def either(x, y):
    if isinstance(x, list):
        raise AttributeError
    if isinstance(y, list):
        raise AttributeError
    return list(x | y)
