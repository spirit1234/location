# -*- coding:utf-8 -*-
class Dog(object):
    def __init__(self, name, age):
        """初始化name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + ' rolled over')


my_dog = Dog('dark', 10)
print('My dog name is ' + my_dog.name + ' and it is ' + str(my_dog.age) + ' years old')
my_dog.sit()
my_dog.roll_over()
