print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))
ticket=0
if height >= 120:
    print("You can ride the rollercoaster")
    if age<12:
        ticket += 5
    elif age >=12 and age <18:
        ticket+=7
    else:
        ticket+=12
    want_photo=input("want photo? Y/N")
    if want_photo=="y" or want_photo=="Y":
        ticket+=3
    else:
        ticket+=0
else:
    print("Sorry you have to grow taller before you can ride.")

print(f"Your total bill: {ticket}")