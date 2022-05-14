"""
    CS5003 Spring 2022
    Lab #5
    03/02/2022
    Jason(Haozhe) Zhang, Vincent Tam
"""


def add_spaces(x='x mustn''t be empty and is a string'):
    i = 0
    my_string = ''
    while(i < len(x)):
        my_string += x[i] + '   '
        i += 1
    return my_string.strip()
