class Application:
    def __init__(self, name, version, cost):
        self.name = name
        self.version = version
        self.cost = cost

    def __repr__(self):
        return f'App({self.name}, {self.version}, {self.cost})'
