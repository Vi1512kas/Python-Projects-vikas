import turtle as t
import random as rd
timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("red")


def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0, 255)
    b = rd.randint(0,255)
    rd_color = (r, g, b)
    return rd_color


timmy.speed(20)


for _ in range(75):
    timmy.pensize(2)
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(5)


screen = t.Screen()
screen.exitonclick()
