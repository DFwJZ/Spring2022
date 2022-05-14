"""
    CS5003 Spring 2022
    Lab #5
    02/23/2022
    Jason(Haozhe) Zhang
"""


def name_number(x):
    idx = 0
    num = 0
    while idx < len(x):
        num += ord(x[idx].lower()) - 96
        idx += 1
    return num
