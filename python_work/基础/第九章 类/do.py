# -*- coding:utf-8 -*-
"""江上清风游，只身醉孤舟。
   遥望秋月远，但知故人秋。
   星夜听寒风，梦中言多愁。
   应知秋夜久，又恐梦无踪。"""

"""餐馆：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，
而后者打印一条消息， 指出餐馆正在营业。"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('This restaurant name is ' + self.name + ' and cuisine_type is ' + self.type)

    def open_restaurant(self):
        print('Restaurant now is in business')


"""实例调用方法describe_restaurant() 。"""
info = Restaurant('Dumplings with help yourself', 'steamed')
info.describe_restaurant()
info.open_restaurant()

""""用户:创建一个名为User 的类，其中包含属性first_name 和last_name ， 还有用户简介通常会存储的其他几个属性。 
在类User 中定义一个名为describe_user() 的方法， 它打印用户信息摘要； 再定义一个名为greet_user() 的方法， 
它向用户发出个性化的问候。创建多个表示不同用户的实例， 并对每个实例都调用上述两个方法。"""


class User(object):
    def __init__(self, first_name, last_name):
        self.st = first_name
        self.ed = last_name

    def describe_user(self):
        print('Your name: %s %s' % (self.st, self.ed))

    def greet_user(self):
        print('Hello ' + self.st + ' ' + self.ed)


name = User('John', 'Conner')
name.describe_user()
name.greet_user()

