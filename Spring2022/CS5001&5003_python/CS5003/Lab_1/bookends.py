"""
    CS5003 Spring 2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa


"""


def main():
    number = int(input("Enter number: "))

    last_digit = number % 10
    first_digit = int(number // 1e3)

    print("The first number is", first_digit)
    print("The last number is", last_digit)


if __name__ == '__main__':
    main()
