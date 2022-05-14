"""
    CS5003 Spring 2022
    Lab #5
    02/23/2022
    Jason(Haozhe) Zhang, Vincent Tam
"""


def fibonacci(x):
    fib_list = []
    a = 1
    b = 1
    if x == 0:
        return fib_list
    elif x == 1:
        fib_list.append(1)
        return fib_list
    elif x == 2:
        fib_list.append(a)
        fib_list.append(b)
        return fib_list

    n = 2
    fib_list.append(a)
    fib_list.append(b)

    while n < x:
        c = a + b
        fib_list.append(c)
        b = a
        a = c
        n += 1
    return fib_list
