from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.write_score()

    def increase_level(self):
        self.level += 1

    def write_game_over(self):
        self.goto(0, 200)
        self.write(f"Game Over", align='center', font=FONT)

    def write_score(self):
        self.goto(-280, 250)
        self.clear()
        self.write(f"Level : {self.level}", align='left', font=FONT)