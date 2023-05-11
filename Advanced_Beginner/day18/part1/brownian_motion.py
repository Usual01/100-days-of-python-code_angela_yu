import turtle
import random


turtle.colormode(255)

miracle = turtle.Turtle()
directions = [0, 90, 180, 270]
color_codes = [(25, 240, 228), (47, 231, 241), (125, 234, 244), (29, 245, 235),
    (13, 160, 109), (27, 212, 113), (134, 167, 191), (48, 104, 142),
    (146, 82, 57), (196, 143, 164), (145, 66, 87), (141, 178, 155), 
    (151, 134, 156), (172, 155, 53), (66, 116, 93), (191, 89, 116), (24, 171, 188),
    (201, 94, 74), (104, 137, 125), (55, 35, 19), (55, 23, 38), 
    (229, 175, 166), (180, 186, 217), (56, 156, 176), (84, 154, 113)]
pens = []
speed = ["fastest", 0, "fast", 10, "normal", 6, "slow", 3, "slowest", 1]
for a in range(1,50):
    pens.append(a)
#miracle.pensize(20)
for m in range(50):
    miracle.speed(random.choice(speed))
    miracle.color(random.choice(color_codes))
    miracle.forward(30)
    miracle.pensize(random.choice(pens))
    miracle.setheading(random.choice(directions))
print(pens)