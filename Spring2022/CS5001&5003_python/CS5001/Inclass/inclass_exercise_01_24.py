

from turtle import *



def equitri(length):
    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)
    right(120)


def square(length):
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)


def main():
    how_big = int(input("How big do you want?\n"))
    equitri(how_big)
    square(how_big)
    print("Done")

if __name__ == '__main__':
    main()
