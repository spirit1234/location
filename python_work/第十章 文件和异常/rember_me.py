# -*- coding:utf-8 -*-
import json


def get_username():
    """定义函数get_username获取username.json文件，
       如果有文件则返回文件中的字符串，没有则返回空值"""
    filename = 'json/username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def add_user():
    """创建username.json文件，内容为你输入的用户名"""
    username = input('What\'s your name: ')
    filename = 'json/username.json'
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        return username


def greet_user():
    """两个函数统一调用"""
    username = get_username()
    if username:
        print("Welcome to back " + username)
    else:
        username = add_user()
        print('We\'ll remember you when you come back ' + username)


greet_user()
