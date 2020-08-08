userId = 0

class User:

    def __init__(self, name, age, email, location='US'):
        global userId
        self.userId = userId + 1
        self.name = name
        self.age = age
        self.email = email
        self.location = location

    def __repr__(self):
        return "User{id} - {name}".format(id=self.userId, name=self.name)

    def __str__(self):
        return "{name} ({age}) - {email}".format(name=self.name, age=self.age, email=self.email)

