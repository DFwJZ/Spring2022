"""    CS5001
    Spring 2022
    Your Name Here (driver) and any partners here (navigator)
"""

import turtle

t1 = turtle.Turtle()


def polygon_helper(n, my_len, angle):
    if n > 0:
        t1.forward(my_len)
        t1.right(angle)
        polygon_helper(n - 1, my_len + 2, angle + 10)


def polygon(n, my_len, howmany):
    polygon_helper(howmany, my_len, 360 / n)


def main():
    # polygon(4, 100)
    polygon(3, 75, 25)
    # polygon(5, 50, 100)


if __name__ == "__main__":
    main()
