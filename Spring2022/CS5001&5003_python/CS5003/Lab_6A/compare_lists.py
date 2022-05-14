"""
    CS5003 Spring 2022
    Lab 6. Problem 8
    Jason(Haozhe) Zhang / Partner
"""


def compare_lists(x, y):
    for i in y:
        for j in x:
            if i == j:
                x.remove(j)
    return len(x) == 0
