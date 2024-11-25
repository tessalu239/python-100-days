from turtle import Turtle

class Score(Turtle):
    def __init__(self,position=(30,220)):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color('white')
        self.write(arg=self.score,font=('Arial',40,'normal'))

    def add_point(self):
        self.score+=1
        self.clear()
        self.write(arg=self.score, font=('Arial', 40, 'normal'))

