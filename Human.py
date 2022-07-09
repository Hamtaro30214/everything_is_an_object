from Animal import Animal


class Human(Animal):
    def __init__(self, fist_name, last_name, species):
        super().__init__(species)
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone = None

    def __repr__(self):
        return f'Human({self.fist_name}, {self.last_name}, {self.phone})'
