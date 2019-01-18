# -*- coding:utf-8 -*-
# 定义一个简单函数


def greet_user():
    print('hello'.title())


greet_user()


# 向函数传递信息
def greet_user1(username):
    print('Hello, ' + username.title() + '!')


greet_user1('john')
'''喜欢的图书 ： 编写一个名为favorite_book() 的函数， 其中包含一个名为title 的形参。 这个函数打印一条消息，
 如One of my favorite books is Alice in Wonderland 。 调用这个函数， 并将一本图书的名称作为实参传递给它。'''


def favorite_book(title):
    print('One of my favorite books is ' + str(title))


favorite_book('The Old Man and the Sea')
