"""
    CS5003 Spring 2022
    Lab 3, Problem to_string
    Jason(haozhe) Zhang / Hui Hu
"""


def build_string(s, x, y, z):

    a = s * x
    b = s * y
    c = s * z

    my_string = a + '\n' + b + '\n' + c

    return my_string
