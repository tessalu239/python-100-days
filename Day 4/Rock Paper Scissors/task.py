from random import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

valid=[rock,paper,scissors]
your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice=random.randint(0,2)

if your_choice==0 or your_choice==1 or your_choice==2 :
    print(valid[your_choice])

    print("Computer chose:")
    print(valid[computer_choice])

    if your_choice==computer_choice:
        print("Even")
    elif( your_choice==0 and computer_choice==2) or (your_choice==2 and computer_choice==1) or (your_choice==1 and computer_choice==0):
        print("You win")
    else:
        print("You loose")
else:
    print("Invalid input")
