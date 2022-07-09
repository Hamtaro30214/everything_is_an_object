from devices.Car import Car


class Electric(Car):
    def __init__(self, producer, model, price):
        super().__init__(producer, model, price)
        self.fuel = 100

    def refuel(self):
        self.fuel = 100
