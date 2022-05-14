"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def calculations():
    n = int(input("Enter the number of values to read: \n"))
    sum = 0
    i = 0
    average = 0.0
    while(i < n):
        num = int(input("Enter an integer: \n"))
        sum += num
        i += 1
        average = num / i
    print("The sum is", sum, '\n')
    print("The average is", average)


def main():
    calculations()


if __name__ == '__main__':
    main()
