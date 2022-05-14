"""
    CS5003 Spring 2022
    Assignment Lab 10-B
    Jason(Haozhe) Zhang

    A program to determine the validity
"""


def get_pos_int():
    # Prompting the user for a positive input
    # try to distinguish the input type, eg. int, float or string
    x = input(" Please enter a positive integer: ")
    try:
        val = int(x)
        # if an int is received, determine the validity by its sign +/-
        if val > 0:
            print(f"get_pos_int returned: {val}")
        else:
            print("Invalid integer input..")
            return get_pos_int()
    # if a string or a float is received, go here
    except ValueError:
        print("Invalid integer input..")
        return get_pos_int()


def main():
    counter = 0
    while counter < 10:
        print(f"Calling get_pos_int from Main.Call Number {counter + 1}")
        get_pos_int()
        counter += 1


if __name__ == '__main__':
    main()
