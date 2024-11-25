from turtle import Turtle, Screen
import time

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
def move_up():
    paddle_1.forward(20)
def move_down():
    paddle_1.backward(20)

paddle_1= Turtle()
paddle_1.penup()
paddle_1.color('white')
paddle_1.setheading(90)
paddle_1.setpos(350,0)
paddle_1.shape('square')
paddle_1.shapesize(stretch_len=5)
screen.onkey(key="Up",fun=move_up)
screen.onkey(key="Down",fun=move_down)
screen.listen()

game_is_on=True
while game_is_on:
    screen.update()


screen.exitonclick()