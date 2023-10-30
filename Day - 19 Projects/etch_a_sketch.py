from turtle import Turtle, Screen
timmy = Turtle()

timmy.color("cyan")
timmy.pensize(20)

def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.back(20)


def move_left():
    timmy.setheading(timmy.heading()+10)


def move_right():
    timmy.setheading(timmy.heading()-10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.bgcolor('black')
screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clear_screen, 'c')
screen.exitonclick()
