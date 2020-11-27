from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        throw = randint(1, self.sides)
        return throw


dice_1 = Die()
throws = 0
for _ in range(10):
    throws += 1
    print (f'Бросок № {throws}:  {dice_1.roll_die()}')