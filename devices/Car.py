from devices.Device import Device


class Car(Device):
    def __init__(self, producer, model, price):
        super().__init__(producer, model, price)

    def __repr__(self):
        return f'Car({self.producer}, {self.model}, {self.price})'

    def turn_on(self):
        return 'Engine started'
