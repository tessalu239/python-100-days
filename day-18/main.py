from random import randint
from turtle import Turtle,Screen
import random

from PIL.ImageChops import screen

# ## Challenge 3: draw multiple shapes
# screen=Screen()
# screen.colormode(255)
# tess=Turtle()
# tess.shape("turtle")
#
# def draw_shapes(n):
#     for g in range(n):
#         tess.forward(100)
#         tess.right(round((360/n)))
#
# def rand_color():
#     r=random.randint(0,255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     return r,b,g
#
# for _ in range (3,10):
#     r,b,g=rand_color()
#     tess.color(r,b,g)
#     draw_shapes(_)
#
# screen.exitonclick()

## RANDOM WALK
# directions=[0,90,180,270,360]
#
# screen=Screen()
# screen.colormode(255)
# tess=Turtle()
# tess.shape("turtle")
# tess.speed(0)
# tess.pensize(10)
#
# for step in range(100):
#     tess.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     tess.setheading(random.choice(directions))
#     tess.forward(30)
#
# screen.exitonclick()


## SPIROGRAPH
# def rand_color():
#     color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     return color
# tess=Turtle()
# tess.shape('turtle')
# screen=Screen()
# screen.colormode(255)
#
# tess.speed('fastest')
# for i in range(0,361,10):
#     tess.color(rand_color())
#     tess.setheading(i)
#     tess.circle(100)
#
# screen.exitonclick()


##HIRST PAINTING
# import colorgram
# colors= colorgram.extract('image.jpg',30)
# hi=[]
# for i in range(len(colors)):
#     rgb=(colors[i].rgb.r,colors[i].rgb.g,colors[i].rgb.b)
#     hi.append(rgb)
#
# print(hi)

color_list=[ (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

tess=Turtle()
my_screen=Screen()
my_screen.colormode(255)
tess.shape('turtle')
tess.speed('fastest')
tess.hideturtle()

#inital pos
tess.penup()
tess.setposition(-100,-100)

for _ in range(10):
    for i in range(10):
        tess.dot(20,random.choice(color_list))
        tess.forward(50)
    tess.backward(500)
    tess.setheading(90)
    tess.forward(50)
    tess.setheading(0)
my_screen.exitonclick()
