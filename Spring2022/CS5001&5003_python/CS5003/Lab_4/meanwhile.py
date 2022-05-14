"""
    CS5003 Spring 2022
    Lab #4B
    02/16/2022
    Jason(Haozhe) Zhang
"""

"""
The print_lower(x) function takes a string as parameter and
convert the only uppercase alphabatic letters to its lowercase,
characters that not in the range a-z or A-Z will be printed without
any further modification.

For example:
>>> print_lower('Hello, world!')
hello, world!

"""


def print_lower(x='x must not be empty, please type in a string'):
    length = len(x)
    string = str(x)
    i = 0
    y = ''

    while (i < length):
        if (ord(string[i]) >= 65 and ord(string[i]) <= 90):
            temp = 32 + ord(string[i])
            y += chr(temp)
            i += 1
        else:
            y += string[i]
            i += 1
    print(y)


"""
The print_upper(x) function takes a string as parameter and
convert the only lower alphabatic letters to its uppercase,
characters that not in the range a-z or A-Z will be printed without
any further modification.

For example:
>>> print_upper('Hello, world!')
HELLO, WORLD!
"""


def print_upper(x='x must not be empty, please type in a string'):
    length = len(x)
    string = str(x)
    i = 0
    y = ''

    while (i < length):
        if (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            temp = ord(string[i]) - 32
            y += chr(temp)
            i += 1
        else:
            y += string[i]
            i += 1
    print(y)


"""
main() function is called only if the meanwhile.py file is opened,
and the print_lower('Hello, world!'), print_upper('Hello, world!')
will be executed.

"""


def main():
    print_lower('Hello, world!')
    print_upper('Hello, world!')


if __name__ == '__main__':
    main()
