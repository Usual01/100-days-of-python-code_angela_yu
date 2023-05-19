import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states50.csv")
all_states = data.state.to_list()
guessed_states = []

# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 were correct", prompt = "What's another state?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()