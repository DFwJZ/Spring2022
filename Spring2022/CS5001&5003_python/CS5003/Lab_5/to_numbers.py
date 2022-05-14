"""
    CS5003 Spring 2022
    Lab #5
    03/02/2022
    Jason(Haozhe) Zhang, Vincent Tam
"""


def to_numbers(x):
    my_list = []
    idx = 0
    while idx < len(x):
        my_list.append(float(x[idx]))
        idx += 1
    return my_list
