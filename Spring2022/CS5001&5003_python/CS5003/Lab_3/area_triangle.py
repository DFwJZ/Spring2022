"""
    CS5003 Spring 2022
    Lab 3, Problem 6
    Jason(haozhe) Zhang / Hui Hu
"""


from math import *


def area_triangle(a, b, c):
    s = (a + b + c) / 2
    area_triangle = sqrt(s * (s - a) * (s - b) * (s - c))

    return area_triangle
