"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def is_bridge(x):
    if not isinstance(x, int):
        raise TypeError
    my_list = [5001, 5002, 5003,
               5004, 5005, 5008,
               5009]
    for course in range(len(my_list)):
        if my_list[course] == x:
            return True
    return False
