# -*- coding:utf-8 -*-
from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 10
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
