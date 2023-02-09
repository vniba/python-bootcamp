class User:
    def __init__(self, ids, username):
        self.id = ids
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


jon = User(1, "jon")
micky = User(2, "micky")
jon.follow(micky)
print(micky.followers)
print(jon.following)
