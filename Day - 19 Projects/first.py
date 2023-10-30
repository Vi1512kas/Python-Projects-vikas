# move turtle 20 times when space pressed.
from turtle import Turtle, Screen
timmy = Turtle()
timmy.color("red")


def move_forward():
    timmy.forward(20)


screen = Screen()
screen.listen()
screen.onkey(move_forward,'space')
screen.exitonclick()
