"""
    CS5003 Spring 2022
    Lab 6. Problem 7
    Jason(Haozhe) Zhang / Partner
"""


def filter_evens(x):
    a = []
    for i in range(len(x)):
        if (not x[i] % 2):
            a.append(x[i])
    return a
