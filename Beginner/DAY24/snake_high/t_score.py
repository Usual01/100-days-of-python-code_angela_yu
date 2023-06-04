from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_SNAKE.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updates()

    def updates(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Arial", 24, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data_SNAKE.txt", mode = 'w') as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.updates()
    
    def increase_score(self):
        self.score += 1
        self.updates() 