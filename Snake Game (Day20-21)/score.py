from turtle import Turtle
FONT=('Courier', 24, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score=0
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=FONT)

    def add(self):
        self.score+=1

    def update(self):
        self.add()
        self.clear()
        self.write(arg=f'Score: {self.score}',move=False, align='center',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER',move=False, align='center',font=FONT)
