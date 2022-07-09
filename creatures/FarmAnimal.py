from creatures.Animal import Animal
from creatures.Edible import Edible


class FarmAnimal(Animal, Edible):
    def __init__(self, species):
        super().__init__(species)

    def be_eaten(self):
        return f'{self} will be eaten'
