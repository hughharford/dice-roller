# dice.py

import random

class Dice():
    def roll(self):
        return random.randint(1,6)


if __name__ == "__main__":
    d = Dice()
    print(d.roll())
