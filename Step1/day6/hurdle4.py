"""
make the robot jump over hurdle if thear is wall minizing lines of code until an just move if clear
"""
def turn_right():
    left()
    left()
    left()

def jump():
    turn_left()
    while wall_on-right():
        move()
        turn_right()
        move()
    while front_is_clear():
        move()
    turn_left()

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()