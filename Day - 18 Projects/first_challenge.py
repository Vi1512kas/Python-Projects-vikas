import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


screen = t.Screen()
screen.exitonclick()
