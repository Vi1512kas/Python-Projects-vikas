import turtle as tr
import random as rd
timmy = tr.Turtle()
colours = ["red", "green", "blue", "yellow", "cyan", "purple"]


def draw_shape(side, col):
    angle = 360/side
    for _ in range(side):
        timmy.color(col)
        timmy.forward(100)
        timmy.right(angle)


for shape_side in range(3,11):
    colo = rd.choice(colours)
    draw_shape(shape_side, colo)
screen = tr.Screen()
screen.exitonclick()
