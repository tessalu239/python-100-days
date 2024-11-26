import time
import random
import threading
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
lv=Scoreboard()
time_speed=0.1
time_create=0.8
screen.listen()
screen.onkey(fun=player.move_forward,key='Up')
car_array=[]
last_car_time = time.time()  # Track the last time a car was generated



create=True

game_is_on = True

while game_is_on:
    current_time=time.time()
    time.sleep(time_speed)
    # Generate a car only every 1 second
    if current_time - last_car_time >= time_create:
        car_array.append(CarManager())
        last_car_time = current_time

    # Move all cars in the array
    for each in car_array:
        each.move()

    #.When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
    if player.ycor()>=280:
        player.reset()
        lv.lv_up()
        time_speed*=0.6
        time_create-=0.2
        if time_create<0.2:
            time_create=0.2

    #When the turtle collides with a car, it's game over and everything stops.
    for each in car_array:
        if player.distance(each)<=28:
            game_is_on=False
            lv.game_over()

    screen.update()
screen.exitonclick()