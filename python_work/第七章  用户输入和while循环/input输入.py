# -*- coding:utf-8 -*-
# python2.7用raw_input()函数
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

# 编写一个跟用户打招呼的程序
name = input('Please input your name: ')
print('Hello ' + str(name))

# 有时候，提示可能超过一行
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("Hello, " + name + "!")