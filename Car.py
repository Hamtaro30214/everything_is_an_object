class Car:
    def __init__(self, producer, model, price):
        self.producer = producer
        self.model = model
        self.price = price

    def __repr__(self):
        return f'Car({self.producer}, {self.model}, {self.price})'
