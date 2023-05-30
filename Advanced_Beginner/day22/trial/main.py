from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()


screen.setup(width=800,height= 700)
screen.bgcolor("green")
screen.title('pong')
screen.tracer(0)

r_paddle = Paddle((385, 0))
l_paddle = Paddle((-385, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "r")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        
screen.exitonclick()