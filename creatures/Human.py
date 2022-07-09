from creatures.Animal import Animal


class Human(Animal):
    def __init__(self, fist_name, last_name, species):
        super().__init__(species)
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone = None
        self.animal = None
        self._balance = 0
        self.garage = []

    def __repr__(self):
        return f'Human({self.fist_name}, {self.last_name}, {self.phone})'

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, money):
        if money < 0:
            raise ValueError('Negative amount money 💰')
        self._balance = money

    @property
    def car(self, index=-1):
        if index + 1 > len(self.garage):
            raise IndexError('No car at given index')
        return self.garage[index]

    @car.setter
    def car(self, vehicle, index=-1):
        self.garage.insert(index, vehicle)

    def value_of_cars(self):
        return sum(car.price for car in self.garage)

    def sort_garage(self):
        self.garage.sort(key=lambda x: x.age)
