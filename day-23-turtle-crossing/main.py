import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

'''
1. creating turtle that move up and down with up and down key
2. generate random turtle in x axis and move in x direction
3. detect collision
4. level up
5. scoreboard
'''

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()


def go_up():
    player.fd(20)


screen.listen()
screen.onkey(go_up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    # detect collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # if player reaches to other corner

    y_cor = player.ycor()
    if y_cor == 280:
        player.goto(0, -280)
        cars.level_up()
        scoreboard.update_score()


screen.exitonclick()
