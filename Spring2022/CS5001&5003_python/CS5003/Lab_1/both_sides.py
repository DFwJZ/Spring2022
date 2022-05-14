"""
    CS5003 Spring 2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    7.Both sides
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():

    entered_value = int(input("Enter value: "))
    if(entered_value >= 0):
        if(entered_value % 2 == 0 or entered_value == 0):
            print("even positive number")
        else:
            print("odd positive number")
    else:
        if(entered_value % 2 == 0):
            print("even negative number")
        else:
            print("odd negative number")


if __name__ == '__main__':
    main()
