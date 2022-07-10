class Device:
    def __init__(self, producer, model, price):
        self.producer = producer
        self.model = model
        self.price = price

    def __repr__(self):
        return f'Device({self.producer}, {self.model}, {self.price})'

    def turn_on(self):
        raise NotImplementedError('Method not implemented')
