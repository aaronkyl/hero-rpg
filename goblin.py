class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2
        
    def attack(self, target):
        target.health -= self.power
        print("The {} does {} damage to you.".format(type(self).__name__.lower(), self.power))