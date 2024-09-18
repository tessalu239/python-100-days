import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#python module
choice=random.choice(friends)
print(choice)

#Using what I already know
rand_index=random.randint(0,len(friends)-1)
print(friends[rand_index])
