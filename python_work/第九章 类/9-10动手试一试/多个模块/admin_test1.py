# -*- coding:utf-8 -*-
from user import User
from admin import Admin
from privileges import Privileges

"""多个模块 ： 将User 类存储在一个模块中， 并将Privileges 和Admin 类存储在另一个模块中。 
再创建一个文件， 在其中创建一个Admin 实例， 并对其调用方法show_privilege() ， 以确认一切都依然能够正确地运行。"""
user1 = Admin('John', 'Conner')
user1.show_privilege()
user2 = User('alice', 'abc')
user2.describe_user()
user3 = Privileges()
user3.show_privileges()
