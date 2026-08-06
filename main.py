from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Check for collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.gen_new_block()
            scoreboard.increase_score()

        # Check for collision with wall
        if snake.head.xcor() > SCREEN_WIDTH / 2 or snake.head.xcor() < SCREEN_WIDTH / -2 or snake.head.ycor() > SCREEN_HEIGHT / 2 or snake.head.ycor() < SCREEN_HEIGHT / -2: 
            scoreboard.game_over()
            game_on = False

        # Check for collision with tail
        for block in snake.snake_blocks[1:]:
            if snake.head.distance(block) < 10:
                scoreboard.game_over()
                game_on = False

    screen.exitonclick()

if __name__ == "__main__":
    main()