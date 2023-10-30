import turtle as tr
timmy = tr.Turtle()
# triangle
for _ in range(3):
    timmy.forward(100)
    timmy.right(120)
# square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
# pentagon
for _ in range(5):
    timmy.forward(100)
    timmy.right(72)
# Hexagon
for _ in range(6):
    timmy.forward(100)
    timmy.right(60)
# Heptagon
for _ in range(7):
    timmy.forward(100)
    timmy.right(51.42)
# Octagon
for _ in range(8):
    timmy.forward(100)
    timmy.right(45)
# Nonagon
for _ in range(9):
    timmy.forward(100)
    timmy.right(40)
# Decagon
for _ in range(10):
    timmy.forward(100)
    timmy.right(36)

screen = tr.Screen()
screen.exitonclick()
