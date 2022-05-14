"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def validating_input():
    try:
        while True:
            x = int(input("Enter value: "))
            if x == 0:
                print("Value should be either negative or positive")
                continue
            y = int(input("Enter value: "))
            if y == 0:
                if x < 0:
                    print("Value should be positive")
                    y = int(input("Enter value: "))
                elif x > 0:
                    print("Value should be negative")
                    y = int(input("Enter value: "))
            if x < 0 and y < 0:
                print("Value should be positive")
                y = int(input("Enter value: "))
            if x > 0 and y > 0:
                print("Value should be negative")
                y = int(input("Enter value: "))
            if x > 0 and y < 0:
                temp = x
                x = y
                y = temp
            # when program reach here x < 0 and y > 0
            break
        print(f"Pair: ({x}, {y})")
    except ValueError:
        print("Please check your input type, they must be integers")


def main():
    validating_input()


if __name__ == '__main__':
    main()
