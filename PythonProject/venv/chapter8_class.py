import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hi, I am {} {}".format(self.firstname, self.lastname))

    def emot(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is little tired today".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))


Maria = Person("Maria", "M", 88, status=True)
Rey = Person("Rey", "J", 100, status=False)
Lee = Person("Lee", "W", 51, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()
