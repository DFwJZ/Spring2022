"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def non_neg():
    is_positive = True

    while (is_positive):
        num = int(input("Enter an integer: \n"))
        if(num >= 0):
            print(num)
        else:
            is_positive = False


def main():
    non_neg()


if __name__ == '__main__':
    main()
