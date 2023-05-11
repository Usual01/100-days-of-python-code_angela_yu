import turtle
import random

turtle.colormode(255)

miracle = turtle.Turtle()
def r_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


miracle.speed('fastest')
def spiro(n):
    for m in range(int(360 / n)):
        miracle.color(r_color())
        miracle.circle(120)
        miracle.setheading(miracle.heading() + 5)
spiro(5)
dont_go = turtle.Screen()
dont_go.exitonclick()