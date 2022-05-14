"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def main():
    a = 0
    b = 1
    print("0\n1")
    in_boundary = True
    while in_boundary:
        c = a + b
        print(c)
        a = b
        b = c
        if c > 1000:
            in_boundary = False


main()
