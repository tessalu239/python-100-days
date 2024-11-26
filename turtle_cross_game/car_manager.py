from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300,random.randint(-270,280))

    def move(self):
            #each.backward(random.randint(1,10))
        self.goto(self.xcor()-MOVE_INCREMENT,self.ycor())

