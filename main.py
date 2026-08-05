from turtle import Screen, Turtle

def setup_screen(): 
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    return screen

def create_snake(): 
    count = 0
    for _ in range(3): 
        snake_block = Turtle("square")
        snake_block.color("white")
        snake_block.goto(count, 0)
        count -= 20

def main(): 
    screen = setup_screen()
    create_snake()
    screen.exitonclick()

if __name__ == "__main__":
    main()