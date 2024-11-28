from turtle import Turtle

POS_X= [0, -20, -40,-60,-80,-100,-120,-140,-160,-180,-200,-220]
class Snake:
    def __init__(self):
        snake_array = []
        for _ in range(3):
            sn = Turtle()
            sn.penup()
            sn.shape('square')
            sn.color('white')
            sn.goto(POS_X[_], 0)
            snake_array.append(sn)
        self.snake=snake_array
        self.len=len(snake_array)
        self.head=self.snake[0]

    def move_up(self):
        if self.head.heading()!= 270:
            self.head.setheading(90)
    def move_down(self):
        if self.head.heading()!= 90:
            self.head.setheading(270)
    def move_left(self):
        if self.head.heading()!= 0:
            self.head.setheading(180)
    def move_right(self):
        if self.head.heading()!= 180:
            self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].pos())
            self.snake[seg_num - 1].forward(20)

    def extent_snake(self):
        sn = Turtle()
        sn.penup()
        sn.shape('square')
        sn.color('white')
        sn.goto(self.snake[len(self.snake)-1].xcor(), self.snake[len(self.snake)-1].ycor()-20)
        self.snake.append(sn)

    def restart_snake(self):
        self.head.home()
        for i in self.snake[3:]:
            i.goto(2000,2000)
        del self.snake[3:]