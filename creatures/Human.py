from creatures.Animal import Animal


class Human(Animal):
    def __init__(self, fist_name, last_name, species):
        super().__init__(species)
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone = None
        self._car = None
        self.animal = None
        self._balance = 0

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
    def car(self):
        return self._car

    @car.setter
    def car(self, vehicle):
        if self.balance > vehicle.price:
            self._car = vehicle
            print('The car was bought with cash')
        elif self.balance > vehicle.price / 12:
            self._car = vehicle
            print('The car was bought on credit')
        else:
            print('You are poor ☹')
