"""
    CS5003 Spring 2022
    Lab #5
    02/23/2022
    Jason(Haozhe) Zhang
"""


def square_each(x):
    idx = 0
    while idx < len(x):
        x[idx] = (x[idx]**2)
        idx += 1
    return x
