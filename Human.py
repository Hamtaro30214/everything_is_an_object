from Animal import Animal


class Human(Animal):
    def __init__(self, fist_name, last_name, species):
        super().__init__(species)
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone = None
        self.car = None
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
