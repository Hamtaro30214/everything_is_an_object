from creatures.Animal import Animal
from devices.Car import Car
from creatures.Human import Human
from devices.Phone import Phone
from devices.Electric import Electric

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
human2 = Human('Jeffrey', "Seller", "Human")
human2.balance = 3500
human.animal = hamster
print(human.animal.sell(human, human2, 1500))
print(human2.balance)
phone1 = Phone('Apple ', 'iPhone 6', 1000, 4.7)
human.phone = phone1
human.phone.sell(human, human2, 900)
print(human.balance)
print(human2.balance)
print(human2.phone)
phone1.install_an_app('BTD6', '31.2', 29.99)
print(phone1.app)
car3 = Electric('Tesla', "X", 70000)
car3.fuel = 4
print(car3.fuel)
car3.refuel()
print(car3.fuel)
