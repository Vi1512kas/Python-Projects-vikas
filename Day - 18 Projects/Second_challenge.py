# drae a dashed line
import turtle as t
timmy = t.Turtle()
timmy.color("red")
for _ in range(10):
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)
    timmy.color("black")


screen = t.Screen()
screen.exitonclick()
