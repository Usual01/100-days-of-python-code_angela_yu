"""
make the robot jump over hurdle if thear is wall minizing lines of code until an just move if clear
"""
def right():
    left()
    left()
    left()

def jump():
    
    left()
    move()
    right()
    move()
    

while not atgoal():
    if wall_in_front():
        jm()
    else:
        move()

