"""
    CS5003 Spring 2022
    Lab #5
    02/16/2022
    Jason(Haozhe) Zhang, Vincent Tam
"""


def convert_tuple(x):
    my_list = []
    if len(x) == 0:
        return my_list
    idx = 0
    while idx < len(x):
        my_list.append(x[idx])
        idx += 1
    return my_list
