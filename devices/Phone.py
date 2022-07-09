from devices.Device import Device


class Phone(Device):
    def __init__(self, producer, model, price, screen_size):
        super().__init__(producer, model, price)
        self.screen_size = screen_size

    def turn_on(self):
        return 'The phone was started'
