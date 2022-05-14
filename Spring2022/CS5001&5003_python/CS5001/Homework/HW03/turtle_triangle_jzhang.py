from turtle import *

"""

"""


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

    first = [x1, y1]
    second = [x2, y2]
    third = [x3, y3]

    """ Initialize the turtle and go to the starting point """
    t.speed(0)
    print("Go to the starting point\n")
    t.penup()
    t.goto(first[0], first[1])
    t.home()
    t.pendown()

    """ start the turtle race"""
    angle1 = t.heading() - t.towards(second[0], second[1])
    dis1 = t.distance(second[0], second[1])
    print("The turtle is at starting point")
    print("current location, x: {}. y: {}".format(t.xcor(), t.ycor()))
    print("next location, x: {}. y: {}".format(second[0], second[1]))
    print("angle1 is {}".format(angle1))
    print("distance is {}\n".format(dis1))
    t.right(angle1)
    t.forward(dis1)

    """ at the second point, need to turn to the third"""
    angle2 = t.heading() - t.towards(third[0], third[1])
    print(towards(third[0], third[1]))
    dis2 = t.distance(third[0], third[1])
    print("The turtle is at second point, and is heading to {0}".format(t.heading()))
    print("towards to {}".format(towards(third[0], third[1])))
    print("current location, x: {}. y: {}".format(t.xcor(), t.ycor()))
    print("next location, third[0]: {}. third[1]: {}".format(third[0], third[1]))
    print("angle3 is {}".format(angle2))
    print("distance is {}\n".format(dis2))
    t.right(angle2)
    t.forward(dis2)

    """ returning to the starting point """
    angle3 = t.heading() - t.towards(first[0], first[1])
    dis3 = t.distance(first[0], first[1])
    print("The turtle is at third point, and is heading to {0}".format(t.heading()))
    print("next location, x: {}. y: {}".format(first[0], first[1]))
    print("next location, first[0]: {}. first[1]: {}".format(first[0], first[1]))
    print("angle3 is {}".format(angle3))
    print("distance is {}\n".format(dis3))
    t.right(angle3)
    t.forward(dis3)
    print("Drawing is complete!\n")
    t.home()
    print("The turtle is back to starting point with starting orientation.")


def main():
    draw_triangle(0, 0, 200, 346.410161514, 400,0)

main()
