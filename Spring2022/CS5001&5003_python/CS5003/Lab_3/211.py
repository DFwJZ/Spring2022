'''
how computer sees the return value?

how computer distinguish the lexicographical order of strings?

eg. 'ab ' and 'aba', is there a hiden charater to be compared in first string?

can we invoke a function without calling it? or the other way around.

'''


def build_string(s, x, y, z):

    a = s * x
    b = s * y
    c = s * z

    my_string = a + '\n' + b + '\n' + c

    return my_string


def main():
    print(build_string('hi', 2, 3, 4))


if __name__ == "__main__":
    main()
