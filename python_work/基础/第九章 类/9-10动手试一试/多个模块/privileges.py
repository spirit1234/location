# -*- coding:utf-8 -*-
class Privileges(object):
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin have these privilege:')
        for i in self.privileges:
            print(i)
