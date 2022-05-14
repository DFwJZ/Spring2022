"""
    CS5003 Spring 2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    6.Clamping
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():

    entered_value = int(input("Enter value: "))

    if(entered_value > 100):
        print("Too big, clamping required")
    elif(entered_value < 1):
        print("Too small, clamping required")
    if(entered_value < 1):
        print("Value is 1")
    elif(entered_value > 100):
        print("Value is 100")
    else:
        print("Value is", entered_value)


if __name__ == '__main__':
    main()
