"""
    CS5003 Spring 2022
    Lab 6, Problem 1
    Jason(Haozhe) Zhang / Partner
"""


def multiples():
    x = int(input("Enter a positive integer: "))
    if x > 0:
        for x in range(5, x + 1, 5):
            print(x)


def main():
    multiples()


if __name__ == '__main__':
    main()
