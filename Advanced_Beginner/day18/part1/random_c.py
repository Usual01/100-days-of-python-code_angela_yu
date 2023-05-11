import turtle
import random

turtle.colormode(255)

miracle = turtle.Turtle()
def r_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

miracle.pensize(20)
miracle.speed('fastest')
directions = [0, 90, 180, 270]

for s in range(200):
    miracle.color(r_color())

    miracle.forward(40)
    miracle.setheading(random.choice(directions))
dont_go = turtle.Screen()
dont_go.exitonclick()