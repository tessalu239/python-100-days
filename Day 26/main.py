# from turtle import Turtle,Screen
#
# timmy= Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
# timmy.back(100)
# timmy.right(90)
# timmy.forward(200)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

table= prettytable.PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align['Pokemon Name']='l'
print(table)