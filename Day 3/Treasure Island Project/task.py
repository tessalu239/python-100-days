print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direct=input('  Type "left" or "right"\n')

if direct =='left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim_or_wait=input('Type "wait" to wait for a boat. Type "swim" to swim across')
    if swim_or_wait=='wait' or swim_or_wait=='Wait':
        print('')
        door_color=input('Choose 1 door color? Red, Yellow, or Blue')
        if door_color=='red' or door_color=='Red':
            print('Burned by fire🔥. Game over')
        elif door_color=='Blue' or door_color=='blue':
            print('Eaten by beasts👹. Game over')
        elif door_color=='yellow' or door_color=='Yellow':
            print('You win')
        else:
            print("Game Over")
    else:
        print('Attacked by trout. Game Over')
else:
    print('Fall into a hole. Game Over😥')

