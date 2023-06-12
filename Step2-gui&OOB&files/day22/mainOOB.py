from turtle import Screen, Turtle
from pongOOB import Paddle
from ball import Ball
from score_board import Scoreboard
import time


screen = Screen()
screen.bgcolor("blue")
screen.setup(width = 730, height = 620)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_len = 1, stretch_wid = 5)
# paddle.penup()
# paddle.goto(350, 0)



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"s")
screen.onkey(l_paddle.go_down,"w")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 299 or ball.ycor() < -299:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
