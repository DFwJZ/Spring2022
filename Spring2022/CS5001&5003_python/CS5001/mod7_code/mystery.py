""" doc string """


def mystery(n, level):
    print("Entering mystery with n =", n)
    if n < 0:
        print("  " * level, "exiting with n =", n, "result =", 2 * n)
        return 2 * n
    else:
        temp = mystery(n - 1, level + 1) + n
        print("  " * level, "exiting with n =", n, "result =", temp)
        return temp


def main():
    print(mystery(3, 0))


if __name__ == '__main__':
    main()
