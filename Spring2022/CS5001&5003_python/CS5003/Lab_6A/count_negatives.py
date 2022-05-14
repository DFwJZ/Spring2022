"""
    CS5003 Spring 2022
    Lab 6. Problem 5
    Jason(Haozhe) Zhang / Partner
"""


def count_negatives(x):
    if not x:
        return 0
    count = 0
    for i in x:
        if i < 0:
            count += 1
    return count
