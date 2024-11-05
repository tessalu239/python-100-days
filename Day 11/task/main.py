import random
import art
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def begin_cards():
    begin=[random.choice(cards),random.choice(cards)]
    if begin[0]==11 and begin[1]==11:
        begin[0]=1
    return begin, sum(begin)

def bot_turn(bot_sum,bot):
    while bot_sum <= 17:
        card = random.choice(cards)
        if card == 11:
            if (bot_sum + card) > 21:
                card = 1
            else:
                card = 10
        bot.append(card)
        bot_sum = sum(bot)

    if bot_sum >= 19 and bot_sum <= 20:
        take_card = 'n'
    else:
        take_card = random.choice(['n', 'y'])

    while bot_sum < 21 and take_card == 'y':
        for n in range(0, len(bot) - 1):
            if bot[n] == 11:
                bot[n] = 10
        card = random.choice(cards)
        if card == 11:
            if (bot_sum + card) > 21:
                card = 1
            else:
                card = 10
        bot.append(card)
        bot_sum = sum(bot)

        if bot_sum >= 19 and bot_sum <= 20:
            take_card = 'n'
        else:
            take_card = random.choice(['n', 'y'])
    return bot_sum,bot

def your_turn(ur_sum,your,bot):
    more_card='y'
    while ur_sum<21 and more_card=='y':
        for i in range(0,len(your)-1):
            if your[i] == 11:
                your[i]=10

        more_card=input(f"Type 'y' to get another card, type 'n' to pass: ")
        if more_card== 'y':
            new_card=random.choice(cards)
            if new_card==11:
                if (ur_sum+new_card) >21:
                    new_card=1
                else:
                    new_card=10
            your.append(new_card)
            ur_sum = sum(your)
            print(f'Your cards: {your}, current score: {ur_sum}')
            print(f"Computer's first card: {bot[0]}")
    return ur_sum,your

def generate_result(ur,bot,ur_sum,bot_sum):
    print(f"Your final hand: {ur}, final score:{ur_sum}")
    print(f"Dealer's final hand: {bot}, final score:{bot_sum}")
    if ur_sum > 21 and bot_sum > 21:
        print("It's a draw, you both go over")
    elif ur_sum > 21:
        print("You loose 🥹 You went over")
    elif bot_sum > 21:
        print("Congrats 💥 You win, Dealer went over")
    else:
        if ur_sum > bot_sum:
            print("Congrats 💥 You win")
        elif ur_sum < bot_sum:
            print("You loose 🥹")
        elif ur_sum == bot_sum:
            print("It's a draw, You guys are equal")

start_game= input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
while start_game=='y':
    print(art.logo)
    yours,your_sum= begin_cards()
    bots, bots_sum= begin_cards()

    print (f'Your cards: {yours}, current score: {your_sum}')
    print(f"Computer's first card: {bots[0]}")
    your_sum,yours=your_turn(your_sum,yours,bots)
    bots_sum,bots=bot_turn(bots_sum,bots)

    #Compare result
    generate_result(yours,bots,your_sum,bots_sum)

    start_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")


