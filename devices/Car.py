from Sellable import Sellable
from devices.Device import Device


class Car(Device, Sellable):
    def __init__(self, producer, model, price, age):
        super().__init__(producer, model, price)
        self.age = age

    def __repr__(self):
        return f'Car({self.producer}, {self.model}, {self.price})'

    def turn_on(self):
        return 'Engine started'

    def refuel(self):
        raise NotImplementedError('Method not implemented')

    def sell(self, seller, buyer, price):
        if self not in seller.garage:
            raise AttributeError("No car in garage 🚗")
        if buyer.balance < price:
            raise ValueError("No money 💰")
        buyer.balance -= price
        seller.balance += price
        seller.garage.remove(self)
        buyer.car = self
        return 'The car has been successfully sold'
