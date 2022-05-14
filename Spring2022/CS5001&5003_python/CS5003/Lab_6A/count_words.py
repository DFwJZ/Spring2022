"""
    CS5003 Spring 2022
    Lab 6. Problem 10
    Jason(Haozhe) Zhang / Partner
"""


def count_words():
    x = str(input("Enter a sentence: "))
    y = x.split(" ")
    for i in range(len(y)):
        print(i, ". ", y[i], sep="")


def main():
    count_words()


if __name__ == '__main__':
    main()
