from turtle import Turtle, Screen
import random
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'violet']
y_cor = [-100, -60, -20, 20, 60, 100]
all_turtles = []
screen = Screen()
screen.setup(height=400, width=900)
user_bet = screen.textinput(title='Choose Option', prompt="Which turtle will win the race? Choose a color : ")
is_game_on = False
for turtle_idx in range(0, len(colors)):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_idx])
    tim.goto(-430, y_cor[turtle_idx])
    all_turtles.append(tim)
if user_bet:
    is_game_on = True
while is_game_on:
    for timmy in all_turtles:
        if timmy.xcor() > 430:
            is_game_on = False
            color_found = timmy.pencolor()
            if user_bet == color_found:
                print(f"You've Won ! {color_found} is the winning color.")
            else:
                print(f"You lose ! {color_found} is the winning color.")
        number = random.randint(0, 10)
        timmy.forward(number)

screen.exitonclick()


