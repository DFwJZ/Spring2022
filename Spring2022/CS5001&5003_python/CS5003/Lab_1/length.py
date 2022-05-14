"""
    CS5003 Spring 2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa

"""


def main():
    meters = float(input("Enter length: "))

    inches = meters * 39.3701
    feet = inches / 12
    miles = feet / 5280

    print("The length in inches is", inches)
    print("The length in feet is", feet)
    print("The length in miles is", miles)


if __name__ == '__main__':
    main()
