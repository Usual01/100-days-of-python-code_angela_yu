from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.pu()
        self.goto(position)
        self.speed("fastest")
        

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
