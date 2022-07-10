from creatures.Animal import Animal
from devices.Application import Application
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
car1 = Car("Audi", "A4", 40000, 2007)
human.car = car1
print(human.car)
human.balance = 3500
print(human.balance)
print(human.car)
car2 = Car("BMW", "M2", 200000, 2013)
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
car3 = Electric('Tesla', "X", 70000, 2020)
car3.fuel = 4
print(car3.fuel)
car3.refuel()
print(car3.fuel)
human.car = car3
car3.owners.append(human)
print(human.value_of_cars())
print(human.garage)
human.sort_garage()
human2.balance = 500000
print(human.garage)
print(human.car.sell(human, human2, 1500))
print(human.car)
print(car3.owners)
print(car3.was_sold_to(human, human2))
print(car3.was_owner(human2))
print(car3.number_of_transactions())
print(car3.was_sold_to(human, human2))
print(car3.transactions)

apple = Phone('Apple', 2020, 4500.0, 16.9)
print(apple.install_an_app('youtube', 'v1.0', 'Google Play'))
BTD6 = Application('BTD6', '31.2', 29.99)
BTD4 = Application('BTD4', '7.8', 4.99)
BTD2 = Application('BTD2', '3.8', 0)
BTD3 = Application('BTD3', '6.9', 0)
BTD7 = Application('BTD7', '1.3', 15.0)
human.phone = apple
human.balance = 1000
print(human.phone.install_new_app(BTD6, human))
print(human.phone.install_new_app(BTD2, human))
print(human.phone.install_new_app(BTD3, human))
print(human.phone.install_new_app(BTD7, human))
print(human.balance)
print(apple.is_installed(BTD6))
print(apple.is_installed_by_name(BTD6.name))
print(apple.is_installed_by_name(BTD4.name))
print(apple.free_applications())
print(apple.get_installed_apps())
print(apple.app_names())
print(human.phone.app_names_by_cost())
