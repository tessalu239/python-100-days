import art
from random import randint

EASY_TURNS=10
HARD_TURNS=5

def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_TURNS
    elif level == 'hard':
        return HARD_TURNS


def compare_numbers(attempts,number):
    while attempts>0:
        guess = int(input("Make a guess: "))
        if guess>number:
            print('Too high.\nGuess again.')
        elif guess<number:
            print("Too low.\nGuess again.")
        elif guess==number:
            return True
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
    return False
def game():
    print(art.logo)
    number=randint(1,100)
    print(number)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempt= set_difficulty()
    print(f"You have {attempt} attempts remaining to guess the number.")

    win=compare_numbers(attempt,number)
    if win:
        print(f'You got it! The answer was {number}')
    else:
        print("You've run out of guesses, you loose")

game()

