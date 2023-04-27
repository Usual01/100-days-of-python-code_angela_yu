"""
make the robot jump over hurdle minizing lines of code until goal is reached
"""
def right():
    left()
    left()
    left()

def jump():
    move()
    left()
    move()
    right()
    move()
    
def jm():
    move()
    jump()
    move()
    jump()
    move()
    jump()
    move()
    jump()
    move()
    jump()
    move()
    jump()


while not at_goal():
    jm()
    
