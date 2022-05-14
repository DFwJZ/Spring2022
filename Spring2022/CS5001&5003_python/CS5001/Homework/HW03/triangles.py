"""
    CS5001 Spring 2022
    Assignment HW03
    Jason(Haozhe) Zhang
"""


from turtle import *


""" turtle screen setup"""
height = 1000
width = 1000
screen = Screen()
screen.screensize(height, width)


def draw_triangle(x1, y1, x2, y2, x3, y3):
    """ draw triangles with given coordinates"""
    t = Turtle()

    """ x_list and y_list to store x and y coordinates"""
    x_ls = []
    y_ls = []

    x_ls.append(x1)
    x_ls.append(x2)
    x_ls.append(x3)

    y_ls.append(y1)
    y_ls.append(y2)
    y_ls.append(y3)

    """ check valid input"""
    for x in x_ls:
        if x < -width / 2 or x > width/2:
            return False
        else:
            continue

    for y in y_ls:
        if y < -height/2 or y > height/2:
            return False
        else:
            continue

    t.speed(1)
    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)


def equitri(x):
    """ draw a triangle with side given as x with factor of 10"""
    Turtle()
    speed(0)
    left(60)
    forward(x * 10)
    right(120)
    forward(x * 10)
    right(120)
    forward(x * 10)
    left(37)


def cool_tri(counter):
    i = 0
    while i <= counter:
        equitri(i)
        i += 1


def distance(x1, y1, x2, y2):
    """ Calculating the distance between two points """
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def perimeter(x1, y1, x2, y2, x3, y3):
    """ Calculating the perimeter of a triangle """
    a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    return a + b + c


def area(x1, y1, x2, y2, x3, y3):
    """ Calculating the area of a triangle given three set of coordinates """
    a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

    s = (a + b + c) / 2

    return (s * (s - a) * (s - b) * (s - c))**0.5


def approx_equal(d1, d2):
    """ Calculating if two distances are equal"""
    is_equal = True
    epsilon = 0.001
    if abs(d1 - d2) >= epsilon:
        is_equal = False
    return is_equal


def approx_isosceles(x1, y1, x2, y2, x3, y3):
    """ Calculating whether a isosceles triangle """
    a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    return approx_equal(a, b) or approx_equal(a, c) or approx_equal(c, b)


def approx_equilateral(x1, y1, x2, y2, x3, y3):
    """ Calculating whether an equilateral triangle """
    a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    return approx_equal(a, b) and approx_equal(a, c) and approx_equal(c, b)


def main():
    """Test for distance function"""
    A_list = [(2, 0, 4, 0),
              (2, 0, 4, 0),
              (2, 0, 4, 0)]

    A_expected_results = [2.0, 4.0, 2.0]

    if len(A_list) != len(A_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    A_actual_results = []
    i = 0
    while i < len(A_list):
        x1 = A_list[i][0]
        y1 = A_list[i][1]
        x2 = A_list[i][2]
        y2 = A_list[i][3]
        A_actual_results.append(distance(x1, y1, x2, y2))
        i += 1

    fail_count = 0
    j = 0
    while j < len(A_expected_results):
        if A_expected_results[j] != A_actual_results[j]:
            fail_count += 1

        print("Test: distance{}\n".format(A_list[j]) +
              "Expected: {}, ".format(A_expected_results[j]) +
              "Atucal :{}\n".format(A_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    """Test for Perimeter function"""
    B_list = [(0, 0, 6, 0, 3, 5.196152422706632),
              (0, 0, 0, 2, 2, 2),
              (0, 0, 6, 0, 3, 5.196152422706632)]

    B_expected_results = [123.0, 6.82842712474619, 23.0]

    if len(B_list) != len(B_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    B_actual_results = []
    i = 0
    while i < len(B_list):
        x1 = B_list[i][0]
        y1 = B_list[i][1]
        x2 = B_list[i][2]
        y2 = B_list[i][3]
        x3 = B_list[i][4]
        y3 = B_list[i][5]
        B_actual_results.append(perimeter(x1, y1, x2, y2, x3, y3))
        i += 1

    fail_count = 0
    j = 0
    while j < len(B_expected_results):
        if B_expected_results[j] != B_actual_results[j]:
            fail_count += 1

        print("Test: Perimeter{}\n".format(B_list[j]) +
              "Expected: {}, ".format(B_expected_results[j]) +
              "Atucal :{}\n".format(B_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    """Test for Area function"""
    C_list = [(-3, 0, 3, 0, 0, 4),
              (0, 0, 3, 0, 0, 4),
              (-3, 0, 3, 0, 0, 4)]

    C_expected_results = [122.0, 6.0, 12.0]

    if len(C_list) != len(C_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    C_actual_results = []
    i = 0
    while i < len(C_list):
        x1 = C_list[i][0]
        y1 = C_list[i][1]
        x2 = C_list[i][2]
        y2 = C_list[i][3]
        x3 = C_list[i][4]
        y3 = C_list[i][5]
        C_actual_results.append(area(x1, y1, x2, y2, x3, y3))
        i += 1

    fail_count = 0
    j = 0
    while j < len(C_expected_results):
        if C_expected_results[j] != C_actual_results[j]:
            fail_count += 1

        print("Test: Area{}\n".format(C_list[j]) +
              "Expected: {}, ".format(C_expected_results[j]) +
              "Atucal :{}\n".format(C_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    """Test approx_equal function"""
    D_list = [(1, 1.001),
              (1, 1.001),
              (5.7, 5.71)]

    D_expected_results = [True, False, False]

    if len(D_list) != len(D_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    D_actual_results = []
    i = 0
    while i < len(D_list):
        d1 = D_list[i][0]
        d2 = D_list[i][1]
        D_actual_results.append(approx_equal(d1, d2))
        i += 1

    fail_count = 0
    j = 0
    while j < len(D_expected_results):
        if D_expected_results[j] != D_actual_results[j]:
            fail_count += 1

        print("Test: approx_equal{}\n".format(D_list[j]) +
              "Expected: {}, ".format(D_expected_results[j]) +
              "Atucal :{}\n".format(D_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    """ Test approx_isosceles function"""
    E_list = [(0, 0, 1, 0, 1, 1.0005),
              (0, 0, 1, 0, 1, 0.95),
              (0, 0, 1, 0, 1, 0.95)]

    E_expected_results = [True, False, True]

    if len(E_list) != len(E_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    E_actual_results = []
    i = 0
    while i < len(E_list):
        x1 = E_list[i][0]
        y1 = E_list[i][1]
        x2 = E_list[i][2]
        y2 = E_list[i][3]
        x3 = E_list[i][4]
        y3 = E_list[i][5]
        E_actual_results.append(approx_isosceles(x1, y1, x2, y2, x3, y3))
        i += 1

    fail_count = 0
    j = 0
    while j < len(E_expected_results):
        if E_expected_results[j] != E_actual_results[j]:
            fail_count += 1

        print("Test: approx_isosceles{}\n".format(E_list[j]) +
              "Expected: {}, ".format(E_expected_results[j]) +
              "Atucal :{}\n".format(E_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    """ Test approx_equilateral function"""
    F_list = [(1, 3, -2.0, 7, 2.964, 7.598),
              (1, 3, -2.0, 7, 2.964, 7.598),
              (1, 3, -2.0, 7, 2.964, 7.598)]

    F_expected_results = [True, False, False]

    if len(F_list) != len(F_expected_results):
        print("The number of acutal results and",
              "the number of expected results are different")
        return

    F_actual_results = []
    i = 0
    while i < len(F_list):
        x1 = F_list[i][0]
        y1 = F_list[i][1]
        x2 = F_list[i][2]
        y2 = F_list[i][3]
        x3 = F_list[i][4]
        y3 = F_list[i][5]
        F_actual_results.append(approx_equilateral(x1, y1, x2, y2, x3, y3))
        i += 1

    fail_count = 0
    j = 0
    while j < len(F_expected_results):
        if F_expected_results[j] != F_actual_results[j]:
            fail_count += 1

        print("Test: approx_equilateral{}\n".format(F_list[j]) +
              "Expected: {}, ".format(F_expected_results[j]) +
              "Atucal :{}\n".format(F_actual_results[j]) +
              "Failed: {}\n".format(fail_count))
        j += 1
    print("Total Failed: {0}".format(fail_count))

    equitri(10)
    cool_tri(40)


if __name__ == '__main__':
    main()
