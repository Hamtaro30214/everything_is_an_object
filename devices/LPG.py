from devices.Car import Car


class LPG(Car):
    def __init__(self, producer, model, price, age):
        super().__init__(producer, model, price, age)
        self.fuel = 60

    def refuel(self):
        self.fuel = 60

