# -*- coding:utf-8 -*-
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


class Privileges(object):
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin have these privilege:')
        for i in self.privileges:
            print(i)
