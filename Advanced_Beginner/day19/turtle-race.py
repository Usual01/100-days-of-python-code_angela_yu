from turtle import Turtle, Screen

dont_go = Screen()

dont_go.setup(800, 600)
user_bet = dont_go.textinput(title="make bet", prompt="who will win")
colors = ["red","orange", "black", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]

for m in range(0, 6):

    miracle = Turtle(shape ="turtle")
    miracle.color(colors[m])
    miracle.penup()
    miracle.goto(x = -380, y = y_positions[m])


dont_go.exitonclick()