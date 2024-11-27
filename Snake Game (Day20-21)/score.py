from turtle import Turtle

from unicodedata import numeric

FONT=('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score=0
        with (open('data.txt',mode='r') as file):
            self.highscore=int(file.read())
        self.write(arg=f'Score: {self.score} High Score: {self.highscore}', move=False, align='center', font=FONT)


    def add(self):
        self.score+=1

    def update(self):
        self.add()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg='GAME OVER',move=False, align='center',font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.highscore}', move=False, align='center', font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        with (open('data.txt',mode='w') as file):
            file.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()


