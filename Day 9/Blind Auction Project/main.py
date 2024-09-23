# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
list_bidder={}
other=True
while other:
    input_name=input("What is your name? ")
    input_bid=int(input("What is your bid?: $"))
    list_bidder[input_name]=input_bid
    answer=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if answer=="no":
        other=False
    if answer=="yes":
        print("\n"*100)
#Python built-in method
winner=max(list_bidder,key=list_bidder.get)
print(f'The highest bid is ${list_bidder[winner]} of {winner}')

#manually
max_bid=0
highest_bidder=""
for each in list_bidder:
    if list_bidder[each]>max_bid:
        max_bid=list_bidder[each]
        highest_bidder=each
print(f'The highest bid is ${max_bid} of {highest_bidder}')


