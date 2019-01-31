# -*- coding:utf-8 -*-
"""冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的
Restaurant 类。这两个版本的Restaurant 类都可以， 添加一个名为flavors 的属性， 用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。 创建一个IceCreamStand 实例， 并调用这个方法。"""
import time
from do import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def writ(self):
        for j in range(int(input('input how many kinds of ice-cream: '))):
            self.flavors.append(input('input kinds of ice-cream: '))
        for i in self.flavors:
            print(i)


ice = IceCreamStand('Dumplings', 'd')
ice.writ()

"""管理员:管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User类。
添加一个名为privileges 的属性， 用于存储一个由字符串（如"can add post" 、 "can delete post" 、 "can ban user" 等）
组成的列表。 编写一个名为show_privileges() 的方法， 它显示管理员的权限。 创建一个Admin 实例， 并调用这个方法。"""


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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privilege(self):
        self.privileges.show_privileges()


"""权限：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。 
将方法show_privileges() 移到这个类中。 在Admin 类中， 将一个Privileges 实例用作其属性。 创建一个Admin 实例， 
并使用方法show_privileges() 来显示其权限。"""


class Privileges(object):
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin have these privilege:')
        for i in self.privileges:
            print(i)


admin = Admin('john', 'Conner')
admin.show_privilege()

"""电瓶升级：给Battery 类添加一个名为upgrade_battery() 的方法。 这个方法检查电瓶容量， 如果它不是85， 
就将它设置为85。 创建一辆电瓶容量为默认值的电动汽车， 调用方法get_range() ，
然后对电瓶进行升级， 并再次调用get_range() 。 你会看到这辆汽车的续航里程增加了"""


class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery(object):
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            mileage = 240
        elif self.battery_size == 85:
            mileage = 270
        message = "This car can go approximately " + str(mileage)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        print('after update battery size: '.title() + str(self.battery_size))


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size=input('input battery size: '))


battery = ElectricCar('a', 'b', 'c')
battery.battery.upgrade_battery()
print('程序运行时间: ' + str(round(time.perf_counter(), 2)) + 's')
