import stdio
import random

#create a data type called "Die" with an insstance variable representing
#the _face_value of the die, a roll_die method and the built-in __str__ method

class Die:
    def __init__(self, face_value):

        self.face_value = face_value

def roll_die(self):
    self.face_value = random.randrange(1,7)

def __str__(self):
    return str(self.face_value)

