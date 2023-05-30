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


game = True
while game:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    
screen.exitonclick()