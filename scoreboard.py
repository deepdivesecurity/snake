from turtle import Turtle
from constants import SCREEN_HEIGHT

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
COLOR = "red"

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, SCREEN_HEIGHT / 2 - 40)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def update_scoreboard(self): 
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self): 
        self.score += 1
        self.update_scoreboard()

    def game_over(self): 
        self.goto(0, 0)
        self.color(COLOR)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)