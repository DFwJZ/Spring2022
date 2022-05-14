"""
    CS5003 Spring 2022
    Lab #5
    02/16/2022
    Jason(Haozhe) Zhang
"""


def diagonal_string(x='x mustn''t be empty and is a string'):
    i = 0
    spaces = ' '
    string = ''
    while(i < len(x)):
        string += i * spaces + x[i] + '\n'
        i += 1
    return string.strip()
