from devices.Car import Car


class LPG(Car):
    def __init__(self, producer, model, price):
        super().__init__(producer, model, price)
        self.fuel = 60

    def refuel(self):
        self.fuel = 60

