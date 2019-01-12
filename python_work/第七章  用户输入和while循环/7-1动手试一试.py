# -*- coding:utf-8 -*-
# 汽车租赁 ： 编写一个程序， 询问用户要租赁什么样的汽车， 并打印一条消息。
car = input('What kind of car do you want to rent?: ')
print('Let me see if I can find you a ' + str(car) +'\n')

# 餐馆订位:编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息， 指出没有空桌；否则指出有空桌。
count = int(input('How many people having food?:'))
if count > 8:
    print('We have no empty table\n')
else:
    print('We have empty tables\n')

# 10的整数倍 ： 让用户输入一个数字， 并指出这个数字是否是10的整数倍。
number = int(input('I can tell you if its ten\'s multiple.\nPlease input a number: '))
if number % 10 == 0:
    print('The number is ten\'s multiple')
else:
    print('The number is not ten\'s multiple')
