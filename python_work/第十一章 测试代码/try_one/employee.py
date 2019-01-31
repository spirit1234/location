# -*- coding:utf-8 -*-
"""雇员 ： 编写一个名为Employee 的类， 其方法__init__() 接受名、 姓和年薪， 并将它们都存储在属性中。
编写一个名为give_raise() 的方法， 它默认将年薪增加5000美元， 但也能够接受其他的年薪增加量。"""


class Employee(object):
    def __init__(self, first_name, last_name, salary):
        self.st = first_name.title()
        self.nd = last_name.title()
        self.salary = salary

    def give_raise(self, adding=5000):
        self.salary += adding
        return self.salary
