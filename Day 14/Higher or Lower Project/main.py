import game_data
import random
import art

def select_from_data():
    choice=random.choice(game_data.data)
    return choice

def compare(a,b):
    if a>b:
        return 'A'
    else:
        return 'B'

def game():
    score=0
    continue_game=True
    a={}
    b={}
    more_followers=''

    while continue_game:
        print(art.logo)
        #decide which data
        if score==0:
            a=select_from_data()
            b=select_from_data()
        else:
            if more_followers=='B':
                a=b
            b = select_from_data()

        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Against B:  {b['name']}, {b['description']}, from {b['country']}")
        more_followers=compare(a['follower_count'],b['follower_count'])
        answer=input("Who has more followers? Type 'A' or 'B': ").upper()

        if answer==more_followers:
            score+=1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game=False

game()
