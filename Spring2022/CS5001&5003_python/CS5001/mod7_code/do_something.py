def do_something(n):
    if n > 0:
        do_something(n - 1)
        print(n, end="")
        do_something(n - 1)


def main():
    """
    Calls the do_something(n) function
    """
    do_something(3)


if __name__ == '__main__':
    main()
