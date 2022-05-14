"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def needs_5002(x, y):
    z = x & y
    print(f"z: {z}")
    who_needs = x - z
    print(who_needs)
    return list(who_needs)


needs_5002({'Riya', 'Nolan'}, {'Ture'})