class User:
    def __init__(self,user_id,username):
        print("creating a new user...")
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def add_follower(self, user):
        self.followers=+1
    def add_following(self, user):
        self.following=+1

user_1=User(1,'tessa')
user_2=User(2,'anders')

#user 1 got a follow from user 2
user_2.add_following(user_1) # 2 go following 1
user_1.add_follower(user_2)  # 1 add 1 follower
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)

#user 1 follow back user 2
user_1.add_following(user_2)
user_2.add_follower(user_1)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)