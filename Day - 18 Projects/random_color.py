import turtle as t
import random as rd
direction = [0, 90, 180, 270]
t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")


def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    rdom_color = (r, g, b)
    return rdom_color


for _ in range(200):
    timmy.speed("fastest")
    timmy.pensize(10)
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(rd.choice(direction))

screen = t.Screen()
screen.exitonclick()