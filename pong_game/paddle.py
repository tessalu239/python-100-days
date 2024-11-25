from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos=(350,0)):
        super().__init__()
        self.penup()
        self.color('white')
        self.setheading(90)
        self.setpos(pos)
        self.shape('square')
        self.shapesize(stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)