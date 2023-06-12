import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')
game = True
while game:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level

screen.exitonclick()