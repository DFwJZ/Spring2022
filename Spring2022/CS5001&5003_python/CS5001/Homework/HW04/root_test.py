"""
    CS5001 Spring 2022
    Assignment HW 04
    Jason(Haozhe) Zhang
"""
from root import *


def test_root():
    passed = 0
    failed = 0
    invalid = 0
    check = False
    while not check:
        str_list = ["1. Testing: root(2, 4) ",
                    "2. Testing: root(3, 27.0, 0.01)",
                    "3. Testing: root(100, 1)",
                    "4. Testing: root(5, 32)",
                    "5. Testing: root(2, -1)",
                    "6. Corner case testing: root(1, 1, 1)",
                    "7. Corner case testing: root(1, 1, 0)",
                    "8. Boundary case testing: root(2, 32, 1)",
                    "9. Edge case testing: root(2, 32, 0.000000000000000001)",
                    "10.Edge case testing: root(1234123, 32)"]

        my_list = [[2, 4, 0.01], [3, 27.0, 0.01], [100, 1, 0.01],
                   [5, 32, 0.01], [2, -1, 0.01], [1, 1, 1],
                   [1, 1, 0], [2, 32, 1], [2, 32, 0.000000000000000001],
                   [123412, 32, 0.01]]

        expected = [2.0, 2.9999, 1.0,
                    2.0, -1, 1,
                    "Invalid", 5.625,
                    "Invalid accuracy input, cannot be less than 1e-14",
                    1.0000028082868084]

        n_list = []
        num_list = []
        accu_list = []
        for i in range(0, len(my_list)):
            n_list.append(my_list[i][0])
            num_list.append(my_list[i][1])
            accu_list.append(my_list[i][2])

        for i in range(0, len(str_list)):
            actual = root(n_list[i], num_list[i], accu_list[i])
            print()
            print("Testing: {}".format(str_list[i]))
            print("Expected: {0}, Actual: {1}".format(expected[i], actual))
            if type(expected[i]) != str or type(actual) != str:
                if abs(actual - expected[i]) < accu_list[i]:
                    passed += 1
                    print("Test passed")
                else:
                    failed += 1
                    print("Test failed, please debug")
            else:
                invalid += 1
                print("Invalid input")

        check = True
    print()
    print("failed:{0} passed:{1} invalid:{2}".format(failed, passed, invalid))


def main():
    print("Root function is designed to calculate the nth root of a number.",
          "It takes three arguments, 'n', 'number', 'accuracy'.\n",
          "Keep in mind:",
          "'n' is an integer>1 representng which roo to calculate.",
          "'number', an integer or float>=1 whose root is to be calculated.",
          "(optional), a float between 0.0 and 1.0, defaulting to 0.001.\n",
          "There are 10 cases in total will be tested.",
          "A case is considered to be a pass case if the difference between",
          "expected and actual result falls in the accuracy range.", sep="\n")
    print()
    x = input("Please press ENTER to initiate the testing for root.....\n")
    test_root()


if __name__ == '__main__':
    main()
