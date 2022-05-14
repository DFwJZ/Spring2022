"""
    CS5003 Spring 2022
    Lab 6. Problem 9
    Jason(Haozhe) Zhang / Partner
"""


def positional_elements(x):
    count = 0
    for i in range(len(x)):
        if i == x[i]:
            count += 1
    return count
