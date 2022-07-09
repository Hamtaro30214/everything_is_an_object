from devices.Car import Car


class Electric(Car):
    def __init__(self, producer, model, price, age):
        super().__init__(producer, model, price, age)
        self.fuel = 100

    def refuel(self):
        self.fuel = 100
