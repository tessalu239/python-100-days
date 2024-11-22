import turtle
from random import randint
from turtle import Turtle,Screen
import random

def create_player(color,locate):
    tur=Turtle()
    tur.shape('turtle')
    tur.color(color)
    tur.penup()
    tur.setx(-230)
    tur.sety(locate)
    tur.speed(random.randint(0,10))
    return tur

my_screen=Screen()
bet=my_screen.textinput('Make your bet','Who will win the race. Enter the color')
my_screen.setup(500,400)


colors=['purple','red','orange','blue','green','yellow']
players=[]
start_pos=100
for color in colors:
    player=create_player(color,start_pos)
    start_pos-=40
    players.append(player)

game_is_on=True
winner=''
while game_is_on:
    for each in players:
        each.forward(random.randint(0,10))
        if each.xcor() >= 220.00:
            game_is_on=False
            winner=each.color()[0]

#print(winner.lower(),bet.lower(),winner.lower()==bet.lower())
if winner.lower()==bet.lower():
    print(f'{winner} turtle is win, Your bet is {bet}, CONGRATS💥')
else:
    print(f'{winner} turtle is win, You are lost')


# print(players)

my_screen.listen()
my_screen.exitonclick()
