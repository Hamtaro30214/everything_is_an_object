import datetime


class Transaction:
    def __init__(self, buyer, seller, price, sell_date=datetime.datetime.now()):
        self.buyer = buyer
        self.seller = seller
        self.price = price
        self.sell_date = sell_date

    def __repr__(self):
        return f'{self.buyer}, {self.seller}, {self.price}, {self.sell_date.strftime("%d/%m/%Y %H:%M:%S")}'





