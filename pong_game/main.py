import time
import random
from turtle import Turtle, Screen
from  paddle import Paddle
from ball import Ball
from score import Score

WINNER_SCORE=5
screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)

divide_line=Turtle()
divide_line.penup()
divide_line.goto(0,-300)
divide_line.pencolor('white')
divide_line.pensize(5)
divide_line.setheading(90)
divide_line.hideturtle()
for i in range(16):
    divide_line.pendown()
    divide_line.forward(20)
    divide_line.penup()
    divide_line.forward(20)

#paddle
paddle_1=Paddle()
paddle_2=Paddle((-350,0))
screen.onkey(key="Up",fun=paddle_1.move_up)
screen.onkey(key="Down",fun=paddle_1.move_down)
screen.onkey(key="w",fun=paddle_2.move_up)
screen.onkey(key="s",fun=paddle_2.move_down)
screen.listen()


#ball
ball=Ball()
#score
score_1=Score()
score_2=Score((-60,220))

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Bounce with wall
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()
    # if ball.xcor()>=380 or ball.xcor()<=-380:
    #     ball.bounce_x()

    #Bounce with paddle
    if ball.distance(paddle_1)<=50 and ball.xcor()>320 or ball.distance(paddle_2)<=50 and ball.xcor()<-320:
        ball.bounce_x()

    #Paddle miss the ball=> game end
    if ball.xcor()>410:
        score_2.add_point()
        time.sleep(1)
        ball.reset_game()
    elif ball.xcor()<-410:
        score_1.add_point()
        time.sleep(1)
        ball.reset_game()


    #Define winner
    if score_2.score==WINNER_SCORE:
        divide_line.goto(-200,0)
        divide_line.write(arg='WINNER', align='center',font=('Arial', 40, 'normal'))
        game_is_on = False
    if score_1.score==WINNER_SCORE:
        divide_line.goto(200, 0)
        divide_line.write(arg='WINNER', align='center', font=('Arial', 40, 'normal'))
        game_is_on = False


screen.exitonclick()