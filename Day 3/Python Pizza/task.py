print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
#Check size
if size=="S" or size=="s":
    bill+=15
    # check add pepperoni for small
    if pepperoni == "Y" or pepperoni == "y":
        bill += 2
    elif pepperoni == "N" or pepperoni == "n":
        bill += 0
elif size=="M" or size=="m":
    bill+=20
    # check add pepperoni for medium/large
    if pepperoni == "Y" or pepperoni == "y":
        bill += 3
    elif pepperoni == "N" or pepperoni == "n":
        bill += 0
elif size=="L" or size=="l":
    bill+=25
    # check add pepperoni for medium/large
    if pepperoni == "Y" or pepperoni == "y":
        bill += 3
    elif pepperoni == "N" or pepperoni == "n":
        bill += 0

#check add pepperoni for small
if extra_cheese=="Y" or extra_cheese=="y":
    bill+=1
elif extra_cheese=="N" or extra_cheese=="n":
    bill+=0

print(f"Your final bill is: ${bill}.")
