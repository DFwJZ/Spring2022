"""
    CS5001 Spring 2022
    Assignment HW03
    Jason(Haozhe) Zhang
"""


from turtle import *


""" turtle screen setup"""
height = 1000
width =1000
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
    cool_tri(50) 

if __name__ == '__main__':
    main()
