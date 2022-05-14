"""
    CS5003 Spring 2022
    Assignment HW04
    Jason(Haozhe) Zhang
"""
from root_test import *


"""
    The root function is designed developed to find
    the nth root of a given number, an optional accuracy
    may be given for additional calculation.

"""


def root(n, number, accuracy=0.001):
    # Exclude the illegal accuracy inputs, must less than 1e-14
    if accuracy < 1e-14:
        return "Invalid accuracy input, cannot be less than 1e-14"
    if n == 1 and number >= 1:
        return number
    # Exclude the illegal number and n inputs, if found, return -1
    if n < 1 or number < 1 or accuracy <= 0.0 or accuracy > 1.0:
        return -1

    # Call the guess function which returns the nth root of the number
    return guess(n, number, accuracy)


"""
    A guess function is created to target the nth root
    of a given number.

    The 'mid' vaiable in first while loop, is equlivalent to
    'root**n' after the second while loop, will be used to
    continuously update either the lower or upper boundary by
    shrinking it down to a smaller interval that the
    root falls in between.

    The second while loop updates the root to a closer
    value to the number
"""


def guess(n, number, accuracy):
    # Two variables 'low', 'high' representaing the searching boundary
    low = 0
    high = number
    # Entering the searching loop
    while low < high:
        # print("low: {0}, high: {1}".format(low, high))
        # Variable 'count' representing the power of 'n'
        count = n
        # Variable 'mid' is calculated as the sum of 'high' and 'low', over 2
        mid = low + (high - low) / 2
        root = 1
        # Converts a new variable 'root' to be 'root**n'
        # by multiplying mid 'n' times
        while count > 0:
            count -= 1
            root *= mid
        # If difference between root**n number less than accuracy, return
        if abs(root - number) < accuracy:
            return mid
        # Forward the lower boundary to be the new mid
        elif root < number:
            low = mid
        # Shrink the upper boundary to be the new mid
        elif root > number:
            high = mid
    # Normally the program won't reach here, return value for abnormal cases
    return -1
