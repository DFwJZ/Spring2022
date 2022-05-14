"""
    CS5003 Spring 2022
    1/26/2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    1.Rectangle
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    area = width * height
    perimeter = 2 * (width + height)
    diagonal = (width ** 2 + height ** 2) ** 0.5

    print("The area of the rectangle is", area)
    print("The perimeter of the rectangle is", perimeter)
    print("The diagonal of the rectangle is", diagonal)


if __name__ == '__main__':
    main()
