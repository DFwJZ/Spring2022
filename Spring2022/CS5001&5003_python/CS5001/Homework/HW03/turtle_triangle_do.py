from turtle import *


"""

"""
def draw_triangle(x1, y1, x2, y2, x3, y3):
    t = Turtle()
    t.speed(1)
    t.penup()
    t.goto(x1, y1)
    t.pendown()

    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)

def main():
    draw_triangle(0, 0, 400, 300, 400,0)

main()
