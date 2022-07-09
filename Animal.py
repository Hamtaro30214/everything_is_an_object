import random


class Animal:
    def __init__(self, species):
        self.species = species
        self.name = None
        if species == 'Dog':
            self.weight = 10.0
        elif species == 'Lion':
            self.weight = 190.0
        elif species == "Human":
            self.weight = 80.0
        else:
            self.weight = 1.0

    def __repr__(self):
        return f'{self.species}'

    def feed(self):
        if self.weight <= 0:
            raise ValueError('Animal is dead ☠')
        self.weight += random.randint(1, 3)
        return "The animal was fed"

    def take_for_a_walk(self):
        if self.weight <= 0:
            raise ValueError('Animal is dead ☠')
        lost_weight = random.randint(2, 4)
        if self.weight - lost_weight < 0:
            self.weight = 0
        else:
            self.weight -= lost_weight
        return 'The animal lost some weight'

