"""
    CS5003 Spring 2022
    Lab 6. Problem 4
    Jason(Haozhe) Zhang / Partner
"""


def calculate_average(x):
    if not x:
        return 0
    list_sum = 0
    for i in x:
        list_sum += i
    return list_sum / len(x)
