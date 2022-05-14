"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""
import initialize

res = initialize.initialize()


def get_key_string(x):
    my_separator = '\n'
    y = my_separator.join(x)
    print(y)
    return y


def main():
    get_key_string(res)


main()
