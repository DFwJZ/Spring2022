"""
    CS5003 Spring 2022
    Lab #5
    02/16/2022
    Jason(Haozhe) Zhang
"""


def list_to_string(x):
    my_string = ''
    idx = 0
    while idx < len(x):
        my_string += str(x[idx]) + '\n'
        idx += 1
    return my_string.strip()
