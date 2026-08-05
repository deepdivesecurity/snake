from turtle import Screen, Turtle
from snake import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def setup_screen(): 
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen

def main(): 
    screen = setup_screen()
    snake = Snake()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    error_message = Turtle()
    error_message.hideturtle()
    error_message.color("red")
    error_message.penup()

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.xcor() > SCREEN_WIDTH / 2 or snake.head.xcor() < SCREEN_WIDTH / -2 or snake.head.ycor() > SCREEN_HEIGHT / 2 or snake.head.ycor() < SCREEN_HEIGHT / -2: 
            error_message.goto(0, 0)
            error_message.write("Game Over", align="center", font=("Arial", 24, "normal"))
            game_on = False

    screen.exitonclick()

if __name__ == "__main__":
    main()