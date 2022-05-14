"""
    CS5003 Spring 2022
    Lab 7. Problem 9
"""


def in_english(x):
    my_dictionary = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                     5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    x = str(x)
    if len(x) == 0:
        return ''
    if len(x) == 1:
        return my_dictionary[int(x[0])]
    return my_dictionary[int(x[0])] + ' ' + in_english(x[1:])
