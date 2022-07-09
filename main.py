from Animal import Animal
from devices.Car import Car
from Human import Human

human = Human('Marcin', 'Rosicki', "Human")
print(human)
human.feed()
print(human.weight)
hamster = Animal('Hamster')
print(hamster.weight)
print(hamster.feed())
print(hamster.take_for_a_walk())
print(hamster.take_for_a_walk())
print(hamster.weight)
car1 = Car("Audi", "A4", 40000)
human.car = car1
print(human.car)
human.balance = 3500
print(human.balance)
print(human.car)
car2 = Car("BMW", "M2", 200000)
human.balance = 250000
human.car = car2
print(human.car)
print(human.car.turn_on())
