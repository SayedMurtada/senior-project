class User:

    def __init__(self, name=None, email=None, Database=[]):
        self.name      = name
        self.email     = email
        self.Database  = Database

# if __name__ == "__main__":
#     user1 = User("c","r","cc")
#     user2 = User()

#     users = []
#     users.append(user1)
#     users.append(user2)

#     print(users[1].name)