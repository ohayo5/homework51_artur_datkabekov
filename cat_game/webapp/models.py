from django.db import models
import random

class Cat:
    AVATARS = {
        "happy": "cat_happy.jpg",
        "neutral": "cat_neutral.jpg",
        "sad": "cat_sad.jpeg",
    }

    def __init__(self, name, age=1, hunger=40, happiness=40, sleeping=False):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.sleeping = sleeping

    def feed(self):
        if self.sleeping:
            return
        self.hunger += 15
        self.happiness += 5
        if self.hunger > 100:
            self.hunger = 100
            self.happiness -= 30
        self._validate()

    def play(self):
        if self.sleeping:
            self.happiness -= 5
            self.sleeping = False
        else:
            self.hunger -= 10
            if random.randint(1, 3) == 1:
                self.happiness = 0
            else:
                self.happiness += 15
        self._validate()

    def sleep(self):
        self.sleeping = True

    def _validate(self):
        self.hunger = max(0, min(self.hunger, 100))
        self.happiness = max(0, min(self.happiness, 100))

    def get_avatar(self):
        if self.happiness >= 70:
            return self.AVATARS["happy"]
        elif self.happiness >= 30:
            return self.AVATARS["neutral"]
        else:
            return self.AVATARS["sad"]
