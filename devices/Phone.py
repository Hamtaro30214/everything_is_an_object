from Sellable import Sellable
from devices.Device import Device


class Phone(Device, Sellable):
    def __init__(self, producer, model, price, screen_size):
        super().__init__(producer, model, price)
        self.screen_size = screen_size
        self.app = None
        self.server = 'https://play.google.com/store/games'
        self.protocol = '8001'
        self.applications = []

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

    def install_an_app(self, name, version, cost):
        self.app = {'name': name, 'version': version, "cost": cost}

    def install_new_app(self, app, user):
        if user.balance < app.cost:
            raise ValueError("No money 💰")
        if app in self.applications:
            raise AttributeError('Application already installed')
        self.applications.append(app)
        user.balance -= app.cost
        return f"App:{app.name} has been installed"

    def is_installed(self, app):
        return app in self.applications

    def is_installed_by_name(self, app_name):
        for app in self.applications:
            if app.name == app_name:
                return True
        return False

    def free_applications(self):
        return [app for app in self.applications if app.cost == 0]

    def get_installed_apps(self):
        return [app for app in self.applications]

    def app_names(self):
        return [app.name for app in sorted(self.applications, key=lambda x: x.name)]

    def app_names_by_cost(self):
        return [app.name for app in sorted(self.applications, key=lambda x: x.cost)]
