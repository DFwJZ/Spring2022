"""
    CS5003 Spring 2022
    Lab 6. Problem 2
    Jason(Haozhe) Zhang / Partner
"""


def count_down():
    for i in range(100, -1, -5):
        if i == 0:
            print("Blastoff!")
        else:
            print(i)
