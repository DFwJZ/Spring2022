# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import validating_input
import validation

def main():
    # print(validation.validation(-3, 4.0))
    # validating_input.validating_input()

    with open('abc.txt') as f:
        for line in f:
            print(line, end='')

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
