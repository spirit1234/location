# -*- coding:utf-8 -*-
class Restaurants(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('This restaurant name is ' + self.name + ' and cuisine_type is ' + self.type)

    # noinspection PyMethodMayBeStatic
    def open_restaurant(self):
        print('Restaurant now is in business')

    def count(self):
        print('There have ' + str(self.number_served) + ' people')

    def set_number_served(self, nu):
        self.number_served = nu
        return nu

    def increment_number_served(self, number):
        while self.number_served < 20:
            self.number_served += number
            print(self.number_served)
        print('Restaurant is crowded')
