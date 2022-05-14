"""
    CS5003 Spring 2022
    Lab 6. Problem 3
    Jason(Haozhe) Zhang / Partner
"""


def count_vowels(x):
    count = 0
    x = x.lower()
    for i in x:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count
