from turtle import Turtle,Screen
import time
from turtledemo.clock import setup
from snake import Snake

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.title("My snake game")
my_screen.bgcolor('black')
my_screen.tracer(0)

my_screen.listen()
snake=Snake()
game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()
    my_screen.onkey(fun=snake.move_up,key="Up")
    my_screen.onkey(fun=snake.move_down,key="Down")
    my_screen.onkey(fun=snake.move_right,key="Right")
    my_screen.onkey(fun=snake.move_left,key="Left")


my_screen.listen()



my_screen.exitonclick()