from turtle import Turtle, Screen

miracle = Turtle()
dont_go = Screen()

def forwards():
    miracle.forward(12)

def backwards():
    miracle.backward(12)

def move_left():
    haed = miracle.heading() + 10
    miracle.setheading(haed)


def move_right():
    haed = miracle.heading() - 10
    miracle.setheading(haed)

def clear():
    miracle.clear()
    miracle.penup()
    miracle.home()
    miracle.pendown()

dont_go.listen()
dont_go.onkey(key="w", fun=forwards)
dont_go.onkey(key="s", fun=backwards)
dont_go.onkey(key="a", fun=move_left)
dont_go.onkey(key="d", fun=move_right)
dont_go.onkey(clear, "c")


dont_go.exitonclick()