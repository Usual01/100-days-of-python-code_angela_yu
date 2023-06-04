import time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for m in starting_positions:
    new_p = Turtle("square")
    new_p.color("white")
    new_p.penup()
    new_p.goto(m)
    segments.append(new_p)

game = True
while game:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) -1, 0, -1):
        new_segx = segments[seg - 1].xcor()
        new_segy= segments[seg - 1].ycor()
        segments[seg].goto(new_segx, new_segy)
    segments[0].forward(20)

screen.exitonclick()