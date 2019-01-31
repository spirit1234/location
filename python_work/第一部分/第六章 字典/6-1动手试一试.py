# -*- coding:utf-8 -*-
'''使用一个字典来存储一个熟人的信息， 包括名、 姓、 年龄和居住的城市。
该字典应包含键first_name 、 last_name 、 age 和city 。
将存储在该字典中的每项信息都打印出来。'''
person1 = {'first_name': 'John', 'last_name': 'Connor', 'age': 18, 'city': 'New York'}
for i, j in person1.items():
    print('{i}:{j}'.format(i=i, j=j))

'''喜欢的数字 ： 使用一个字典来存储一些人喜欢的数字。 请想出5个人的名字， 并将这些名字用作字典中的键；
 想出每个人喜欢的一个数字， 并将这些数字作为值存储在字典中。 打印每个人的名字和喜欢的数字。'''
number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for nu, name in number.items():
    print(nu+'\'s favorite number is ' + str(name))

