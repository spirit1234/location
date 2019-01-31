# -*- coding:utf-8 -*-
filename = 'jjq.txt'

with open(filename, 'w') as file_obj:
    file_obj.write("My name is jjq")

"""访客 ： 编写一个程序， 提示用户输入其名字； 用户作出响应后， 将其名字写入到文件guest.txt中。"""
boo = True
print('Input q to exit')
while boo:
    user_name = input('Please input your name: ')
    if user_name == 'q':
        boo = False
    file_name = 'guest.txt'

    with open(file_name, 'a') as file_object:
        file_object.write(user_name + '\n')
        print('Already been added')
