import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# screen setup
screen = Screen()
screen.title("Game")
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

# calling objects
player = Player()
car_manager = CarManager()
score = Scoreboard()
# listening keyboard
screen.listen()
screen.onkey(player.move_up, 'Up')

# playing game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    player.write('')
    # Detect Collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.write_game_over()
    # at end line
    if player.is_at_finish_line():
        car_manager.level_up()
        score.increase_level()
        score.write_score()
        player.goto_start()
screen.exitonclick()
