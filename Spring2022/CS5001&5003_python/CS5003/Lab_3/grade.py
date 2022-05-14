"""
    CS5003 Spring 2022
    Lab 3, Problem 7
    Jason(haozhe) Zhang / Hui Hu
"""


def grade(a):

    if(a >= 93.00 and a <= 100.00):
        fgrade = 'A'
    elif(a >= 90.00 and a <= 92.99):
        fgrade = 'A-'
    elif(a >= 86.00 and a <= 89.99):
        fgrade = 'B+'
    elif(a >= 82.00 and a <= 85.99):
        fgrade = 'B'
    elif(a >= 77.00 and a <= 81.99):
        fgrade = 'B-'
    elif(a >= 73.00 and a <= 76.99):
        fgrade = 'C+'
    elif(a >= 69.00 and a <= 72.99):
        fgrade = 'C'
    elif(a >= 65.00 and a <= 68.99):
        fgrade = 'C-'
    else:
        fgrade = 'F'

    return fgrade
