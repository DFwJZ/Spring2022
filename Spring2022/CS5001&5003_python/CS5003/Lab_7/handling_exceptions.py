"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


import random
random.seed(0)


def generate_random_error():
    value = random.randint(0, 3)
    if value == 0:
        print(f"Zero division error -- {value}")
    elif value == 1:
        print(f"Type error raised   -- {value}")
    elif value == 2:
        print(f"Value error raised  -- {value}")
    else:
        print(f"Name error raised   -- {value}")


def main():
    for i in range(20):
        generate_random_error()


if __name__ == '__main__':
    main()
