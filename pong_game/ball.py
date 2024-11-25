import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move_y=10
        self.move_x=10

    def move(self):
        x = self.xcor() + self.move_x
        y= self.ycor() + self.move_y
        self.goto(x,y)

    def bounce_y(self):
        self.move_y*=-1

    def bounce_x(self):
        self.move_x*=-1

    def bounce_paddle(self):
        rand_x=random.choice([-1])
        self.move_x*=rand_x
        rand_y=random.choice([1,-1])
        self.move_y*=rand_y

    def reset_game(self):
        self.home()
        self.bounce_x()


