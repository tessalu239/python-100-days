import random
#way 1
coin_flip=['Heads','Tails']
print(random.choice(coin_flip))

#way 2
rand_num=random.randint(0,1)
if rand_num==0:
    print("Heads")
elif rand_num==1:
    print("Tails")