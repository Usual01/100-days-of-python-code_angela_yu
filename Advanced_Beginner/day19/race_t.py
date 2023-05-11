from turtle import Turtle, Screen
import random
dont_go = Screen()

race_on = False
dont_go.setup(800, 600)
user_bet = dont_go.textinput(title="make bet", prompt="who will win")
colors = ["red","orange", "black", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for m in range(0, 6):

    miracle = Turtle(shape ="turtle")
    miracle.color(colors[m])
    miracle.penup()
    miracle.goto(x = -380, y = y_positions[m])
    all_turtle.append(miracle)

if user_bet:
     race_on = True


while race_on:
     for t in all_turtle:
        if t.xcor() > 370:
            race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} won")
            else:
                print(f"{winning_color} won, you lost")
            
        rand_d = random.randint(0, 10)
        t.forward(rand_d)
dont_go.exitonclick()