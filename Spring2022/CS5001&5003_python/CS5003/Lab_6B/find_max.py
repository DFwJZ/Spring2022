"""
    CS5003 Spring 2022
    Lab 7. Problem 7
"""


def find_max(ls):
    if len(ls) == 1:
        return ls[0]
    max_num = find_max(ls[1:])
    return helper(ls[0], max_num)


def helper(cur_max, new_num):
    if new_num > cur_max:
        cur_max = new_num
    return cur_max
