import turtle as t
import random as rd
colours = ["red", "green", "blue", "yellow", "cyan", "purple", "pink"]
direction = [0, 90, 180, 270]
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
for _ in range(200):
    timmy.speed("fastest")
    timmy.pensize(15)
    timmy.color(rd.choice(colours))
    timmy.forward(50)
    timmy.setheading(rd.choice(direction))




screen = t.Screen()
screen.exitonclick()