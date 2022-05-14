"""
    CS5003 Spring 2022
    Assignment Lab 8 Module 11
    Jason(Haozhe) Zhang and Manu Singh and Yuan wang
"""


def make_string_set(x):
    if len(x) == 0:
        return set(x)
    else:
        new_str = x.replace(", ,", ",")
        lst = new_str.split(", ")
        ret_set = set(lst)
    return ret_set
