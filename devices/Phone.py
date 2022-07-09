from Sellable import Sellable
from devices.Device import Device


class Phone(Device, Sellable):
    def __init__(self, producer, model, price, screen_size):
        super().__init__(producer, model, price)
        self.screen_size = screen_size

    def turn_on(self):
        return 'The phone was started'

    def sell(self, seller, buyer, price):
        if self != seller.phone:
            raise AttributeError("No phone 📱")
        if buyer.balance < price:
            raise ValueError("No money 💰")
        buyer.balance -= price
        seller.balance += price
        seller.phone = None
        buyer.phone = self
        return 'The phone has been successfully sold'
