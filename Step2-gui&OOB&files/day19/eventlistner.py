from turtle import Turtle, Screen

miracle = Turtle()
dont_go = Screen()

def move_forwards():
    miracle.forward(12)

dont_go.listen()
dont_go.onkey(key="space", fun=move_forwards)
dont_go.exitonclick()