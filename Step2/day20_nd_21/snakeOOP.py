import time
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_seg(pos)


    def add_seg(self, pos):
        new_p = Turtle("square")
        new_p.color("white")
        new_p.penup()
        new_p.goto(pos)
        self.segments.append(new_p)
    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            new_segx = self.segments[seg - 1].xcor()
            new_segy= self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_segx, new_segy)
        self.head.forward(MOVE_D)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

