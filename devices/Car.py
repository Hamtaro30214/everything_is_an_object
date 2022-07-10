from Sellable import Sellable
from devices.Device import Device
from devices.Transaction import Transaction


class Car(Device, Sellable):
    def __init__(self, producer, model, price, age):
        super().__init__(producer, model, price)
        self.age = age
        self.owners = []
        self.transactions = []

    def __repr__(self):
        return f'Car({self.producer}, {self.model}, {self.price})'

    def turn_on(self):
        return 'Engine started'

    def refuel(self):
        raise NotImplementedError('Method not implemented')

    def sell(self, seller, buyer, price):
        if self not in seller.garage:
            raise AttributeError("No car in garage 🚗")
        if self.owners[-1] != seller:
            raise IndexError("Seller isn't the last owner of the car")
        if buyer.balance < price:
            raise ValueError("No money 💰")
        buyer.balance -= price
        seller.balance += price
        seller.garage.remove(self)
        buyer.car = self
        self.owners.append(buyer)
        self.transactions.append(Transaction(buyer, seller, price))
        return 'The car has been successfully sold'

    def was_owner(self, human):
        return human in self.owners and self.owners[-1] != human

    def number_of_transactions(self):
        return len(self.owners)

    def was_sold_to(self, seller, buyer):
        for index, owner in enumerate(self.owners):
            if owner == buyer and self.owners[index - 1] == seller:
                return True
        return False
