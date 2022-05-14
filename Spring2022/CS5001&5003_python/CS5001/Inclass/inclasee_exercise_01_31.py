"""
    CS5003 Spring 2022
    01/31/2022 Lecture 2
    inclass notes
"""
import turtle

def turtle():

    loadWindow = turtle.Screen()
    turtle.speed(2)
 
    for i in range(100):
        turtle.circle(5*i)
        turtle.circle(-5*i)
        turtle.left(i)
 
    turtle.exitonclick()


def pizza():
    pizzas = int(input("How many pizzas did you order? \n"))
    people = int(input("How many people are there? \n"))
    if people != 0:
        slices = pizzas / people
        print(people, "people", "will each have", slices, "slices of pizza", sep=' ')

    else:
        print("People cannot be 0")


def number():
    number = int(input("Enter integer between 1 and 5 (inclusive) \n"))
    answer = "Not in range"

    if number == 1:
        answer = "One"
    elif number == 2:
        answer = "Two"
    elif number == 3:
        answer = "Three"
    elif number == 4:
        answer = "Four"
    elif number == 5:
        answer = "Five"

    print(answer)


def month():
    month = input("Enter month: ")
    if month == "Feb":
        days = 28
    elif month == "Sep" or month == "Apr" or month == "Jun" or month == "Nov":
        days = 30
    else:
        days = 31
    print(month, "has", days, "days", sep=' ')


def reading():
    reading = int(input("Enter grade for readings: "))
    labs = int(input("Enter grade for labs: "))
    hw = int(input("Enter grade for hw: "))
    exams = int(input("Enter grade for exams: "))

    read_part = reading * 5
    lab_part = labs * 15
    hw_part = hw * 50
    exam_part = exams * 30
    average = (read_part + lab_part + hw_part + exam_part) / 100

    print("Average is ", average)    


def truth_table():
    for i in range (2):
        for j in range (2):
            for k in range (2):
                print(k)
def main():

    truth_table() 


if __name__ == '__main__':
    main()
