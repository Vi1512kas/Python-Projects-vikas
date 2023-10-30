# def add(a, b):
#     return a+b
#
#
# def minus(a, b):
#     return a-b
#
#
# def multiply(a, b):
#     return a*b
#
#
# def divide(a, b):
#     return a/b
#
#
# def operation(a, b, fun):
#     return fun(a, b)
#
#
# print(operation(10, 20, add))
# move turtle 20 times when space pressed.
from turtle import Turtle, Screen
timmy = Turtle()
tim = Turtle()
timmy.color("red")
tim.color("black")


def move_forward():
    timmy.forward(20)
    tim.back(20)


screen = Screen()
screen.listen()
screen.onkey(move_forward,'space')
screen.exitonclick()
