class User :
    def __init__(self,user_id,user_name) :
        self.id = user_id
        self.name = user_name
        self.followers= 0
        self.following=0

    def follow(self,user):
        user.followers +=1
        self.following +=1

user1 = User(100, "abdul")
user2 = User(200, "venkat")
user1.id = 102

print(user1.id)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)