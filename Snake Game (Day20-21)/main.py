from turtle import Screen
import time
from turtledemo.clock import setup
from snake import Snake
from food import Food
from score import Score

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.title("My snake game")
my_screen.bgcolor('black')
my_screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

my_screen.listen()
my_screen.onkey(fun=snake.move_up,key="Up")
my_screen.onkey(fun=snake.move_down,key="Down")
my_screen.onkey(fun=snake.move_right,key="Right")
my_screen.onkey(fun=snake.move_left,key="Left")
game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    #Check if snake eats the food
    if snake.head.distance(food) <15:
        print('nom nom nom')
        food.new_location()
        score.update()
        snake.extent_snake()

    # Gameover when snake hits the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290:
        game_is_on=False
        score.game_over()

    # Gameover if snake eating itself
    for i in snake.snake[1:]:
        if snake.head.distance(i)<10:
            game_is_on = False
            score.game_over()




my_screen.exitonclick()