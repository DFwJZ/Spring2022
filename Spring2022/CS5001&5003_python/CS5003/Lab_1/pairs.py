"""
    CS5003 Spring 2022
    01/26/2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    8.Pairs
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():

    a, b, c, d = input("Enter value: ").split()

    part1 = int(a) + int(b) - int(c) - int(d)
    part2 = int(a) + int(c) - int(b) - int(d)

    if(part1 == 0 or part2 == 0):
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == '__main__':
    main()
