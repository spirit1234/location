# -*- coding:utf-8 -*-
"""就餐人数 ： 在为完成练习9-1而编写的程序中， 添加一个名为number_served 的属性， 并将其默认值设置为0。
根据这个类创建一个名为restaurant 的实例； 打印有多少人在这家餐馆就餐过， 然后修改这个值并再次打印它。
添加一个名为set_number_served() 的方法， 它让你能够设置就餐人数。 调用这个方法并向它传递一个值， 然后再次打印这个值。
添加一个名为increment_number_served() 的方法， 它让你能够将就餐人数递增。 调用这个方法并向它传递一个这样的值： 你认为这家餐馆每天可能接待的就
餐人数。"""


class Restaurant(object):
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


restaurant = Restaurant('dumplings', 'steamed')
restaurant.number_served = 1
restaurant.count()
restaurant.set_number_served(2)
restaurant.count()
restaurant.increment_number_served(1)

"""在为完成练习9-3而编写的User 类中， 添加一个名为login_attempts 的属性。 编写一个名为increment_login_attempts() 
的方法，它将属性login_attempts 的值加1。 再编写一个名为reset_login_attempts() 的方法， 它将属性login_attempts 的值
重置为0。根据User 类创建一个实例， 再调用方法increment_login_attempts() 多次。 打印属性login_attempts 的值， 确认它
被正确地递增； 然后， 调用方法reset_login_attempts() ， 并再次打印属性login_attempts 的值， 确认它被重置为0。"""


class User(object):
    def __init__(self, first_name, last_name):
        self.st = first_name
        self.ed = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('Your name: %s %s' % (self.st, self.ed))

    def greet_user(self):
        print('Hello ' + self.st + ' ' + self.ed)

    def increment_login_attempts(self, num):
        for i in range(num):
            self.login_attempts += 1
            print('已登录' + str(self.login_attempts) + '次')

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user = User('John', 'Conner')
user.increment_login_attempts(5)
user.reset_login_attempts()
print(user.reset_login_attempts())
