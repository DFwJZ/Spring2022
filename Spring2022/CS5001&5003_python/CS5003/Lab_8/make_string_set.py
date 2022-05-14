"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def make_string_set(x):
    if len(x) == 0:
        return set('')
    my_list = x.replace(",", '')
    my_list = my_list.split()
    return set(my_list)
