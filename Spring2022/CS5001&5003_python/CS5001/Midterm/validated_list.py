"""
    CS5001 Spring 2022
    Midterm
    Jason(Haozhe) Zhang
"""
from number_checks import *


def validated_list():
    my_list = []
    while True:
        str1 = input("Please enter a positive int or float less than 100: ")
        if int_ok(str1):
            str_int = int(str1)
            if str_int <= 0 or str_int >= 100:
                print("Invalid entry (ignored). Please try again.")
                str1
            else:
                print("Ok. You entered {}".format(str_int))
                my_list.append(str_int)
        elif float_ok(str1):
            str_float = float(str1)
            if str_float <= 0.0 or str_float >= 100.0:
                print("Invalid entry (ignored). Please try again.")
                str1
            else:
                print("Ok. You entered {}".format(str_float))
                if str_float.is_integer():
                    my_list.append(int(str_float))
                else:
                    my_list.append(str_float)
        else:
            print("Done")
            return my_list


def test_validated_list():
    validated_list()
    passed = 0
    failed = 0
    while True:
        print("Testing the validated_list function: ",
              "Please enter a number as intructed: ",
              "1. Testing function with input of [0, -1, 1, 99.0, 3.14, 100] ",
              "2. Testing function with input of [9, 12, 11.1, 12.9]",
              "3. Testing function with no input, press Enter", sep="\n")
        action = int(input("Enter a number: "))

        test_list = [[1, 99, 3.14],
                     [9, 12, 11.1, 12.9],
                     []]

        if action == 1:
            print("User chooses 1, now start testing\n",
                  "Enter each element in the following list:",
                  "[0, -1, 1, 99.0, 3.14, 100]", sep="\n")
            actual_list = validated_list()
            if actual_list == test_list[0]:
                passed += 1
                print("Test passed")
            else:
                failed += 1
                print("Test failed, check your input or debug the function")

        if action == 2:
            print("User chooses 2, now start testing\n",
                  "Enter each element in the following list:",
                  "[9, 12, 11.1, 12.9]",
                  "Press enter when finished type", sep="\n")
            actual_list = validated_list()
            if actual_list == test_list[1]:
                passed += 1
                print("Test passed")
            else:
                failed += 1
                print("Test failed, check your input or debug the function")

        if action == 3:
            print("User chooses 3, now start testing\n",
                  "Press Enter", sep="\n")
            actual_list = validated_list()
            if actual_list == test_list[2]:
                passed += 1
                print("Test passed")
            else:
                failed += 1
                print("Test failed, check your input or debug the function")
        print("failed : {0}, passed : {1}".format(failed, passed))


def main():
    x = int(input("How many times would you like to test ?"))
    while True:
        if x == 0:
            break
        else:
            test_validated_list()
            x -= 1


if __name__ == '__main__':
    main()
