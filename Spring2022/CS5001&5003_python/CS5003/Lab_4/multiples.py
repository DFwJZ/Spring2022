"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def multiples():
    num = int(input('Enter a non-zero integer: \n'))
    multiple = int(input('Enter multiple: \n'))

    while multiple % num != 0:
        multiple = int(input('Try again: \n'))


def main():
    multiples()


if __name__ == '__main__':
    main()
