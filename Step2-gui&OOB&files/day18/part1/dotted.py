from turtle import Turtle, Screen

miracle = Turtle() 
def draw():
    for m in range(5):
        miracle.forward(10)
        miracle.penup()
        miracle.forward(10)
        miracle.pendown()
    
def move():
    draw()
    miracle.left(90)

for m in range(4):
    move()