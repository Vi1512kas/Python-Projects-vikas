# import colorgram
# colors = colorgram.extract("image.jpg",10)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col = (r, g, b)
#     color_list.append(col)
# print(color_list)
import turtle as tr
import random
tr.colormode(255)
color_list = [(16, 8, 4), (7, 22, 59), (58, 6, 34), (13, 108, 199), (177, 7, 64), (202, 163, 7), (160, 84, 28),
              (16, 35, 159), (210, 224, 244), (246, 233, 208)]
timmy = tr.Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.penup()
timmy.forward(350)
timmy.pendown()
timmy.setheading(0)
for i in range(1,101):
    tr.hideturtle()
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    if i %10 == 0:
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.setheading(180)
        timmy.penup()
        timmy.forward(500)
        timmy.pendown()
        timmy.setheading(0)
screen = tr.Screen()
screen.exitonclick()

