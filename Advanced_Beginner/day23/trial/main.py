import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game = True
while game:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game = False

        if player.is_at_finish():
            player.go_to_start()
            car.level_up()

screen.exitonclick()