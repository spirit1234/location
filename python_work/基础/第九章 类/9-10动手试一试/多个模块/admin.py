# -*- coding:utf-8 -*-
from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privilege(self):
        self.privileges.show_privileges()
