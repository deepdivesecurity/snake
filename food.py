from turtle import Turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

x = (SCREEN_WIDTH // 2 - 20) * -1
y = (SCREEN_HEIGHT // 2 - 20)

class Food(Turtle): 
    def __init__(self): 
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        
        print(x, y)
        self.goto(random.randint(x, y), random.randint(x, y))

    def refresh(self): 
        self.goto(random.randint(x, y), random.randint(x, y))
