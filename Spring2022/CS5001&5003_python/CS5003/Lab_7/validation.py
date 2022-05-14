"""
Write a function called validation that satisfies the following description.
Be sure to code it defensively

Function: validation
   perform multiplication with different types
Parameters:
   one. an negative integer value
   two. a positive floating point number less than 1000
Returns the product of the two parameter values

    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def validation(x, y):
    if not isinstance(x, int) or not isinstance(y, float):
        raise TypeError
    if x >= 0 or y >= 1000 or y <= 0:
        raise ValueError
    else:
        return x * y


print(validation(-3, 100.12))
