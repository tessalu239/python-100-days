from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,260)
        self.hideturtle()
        self.lv=1
        self.write(arg=f'Level: {self.lv}',font=FONT)

    def lv_up(self):
        self.lv+=1
        self.clear()
        self.write(arg=f'Level: {self.lv}',font=FONT)

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER',align='center',font=FONT)



