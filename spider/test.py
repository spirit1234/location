#!/usr/bin/env python
# coding: utf-8

# # 打印1-100之间所有的奇数

# In[12]:


for i in range(1, 100):
    if i % 2 == 1:
        print(i)


# # 去除字符串中的字符

# In[19]:


# -*- coding:utf-8 -*-

word = "你好$$$我正在学 Python@#@现在需要&*&*修改字符串"

# 方法一
print(
    word.replace('$', ' ').replace('@', ' ').replace('#', ' ').replace(
        '&', ' ').replace('*', ' '))

# 方法二
import re
print(re.sub('[@#$*&]', ' ', word))


# # 9乘9乘法口诀表

# In[5]:


# 第一种方法
def first_idea():
    for i in range(1, 10):
        j = 1
        print('\n')
        while j <= i:
            k = i * j
            print((str(j) + ' * ' + str(i) + ' = ' + str(k)), end='  ')
            j += 1
    print('\n')


# 第二种方法
def second_idea():
    for i in range(1, 10):
        for j in range(1, i + 1):
            sum1 = i * j
            if j < i:
                print(('%s * %s = %s' % (j, i, sum1)), end='  ')
            else:
                print('%s * %s = %s' % (j, i, sum1))


first_idea()
second_idea()


# # 奖金与利润提成

# In[62]:


"""请写出一个函数，当输入函数变量月利润为I时，能返回应发放奖金
的总数。例如，输出“利润为100000元时，应发放奖金总数为10000元”
其中，企业发放的奖金根据利润提成。利润（I)低于或等于10万元时，奖
金可提10‰;利润高于10万元，低于20万元时，低于10万元的部分按10％提
成，高于10万元的部分，可提成7.5％：利润在20万元到40万元之间时，高于
20万元的部分可提成5％；利润在40万元到60万元之间时，高于40万元的部分
可提成3％；利润在60万元到100万元之间时，高于60万元的部分可提成
1.5‰利润高于100万元时，超过100万元的部分按1％提成。"""

# 第一种方法
def bonus():
    bonus = 0
    num = int(input('please input your monthly profit(ten thousand): '))
    if num <= 10:
        bonus = num * 0.1
        return bonus
    elif num > 10 and num < 20:
        bonus = (10 * 0.1) + (num - 10) * 0.075
        return bonus
    elif num > 20 and num < 40:
        bonus = (10 * 0.1) + (10 * 0.075) + (num - 20) * 0.05
        return bonus
    elif num > 40 and num < 60:
        bonus = (10 * 0.1) + (10 * 0.075) + (20 * 0.05) + (num - 40) * 0.03
        return bonus
    elif num > 60 and num < 100:
        bonus = (10 * 0.1) + (10 * 0.075) + (20 * 0.05) + (
            20 * 0.03) + (num - 60) * 0.015
        return bonus
    elif num > 100:
        bonus = (10 * 0.1) + (10 * 0.075) + (20 * 0.05) + (20 * 0.03) + (
            40 * 0.015) + (num - 100) * 0.001
        return bonus
    else:
        return 'error'


print(str(bonus() * 10000) + '￥')


# 第二种方法
class Jjq():
    def __init__(self, nu):
        self.ten = 10 * 0.1
        self.ten_twe = 10 * 0.075
        self.twe_forty = 20 * 0.05
        self.forty_sixty = 20 * 0.003
        self.sixty_tens = 40 * 0.015
        self.nu = nu

    def under_ten(self):
        return (self.nu - 10) * 0.1

    def ten_twen(self):
        return self.ten + (self.nu - 10) * 0.075

    def twen_forty(self):
        return self.ten + self.ten_twe + (self.nu - 20) * 0.05

    def four_sixty(self):
        return self.ten + self.ten_twe + self.twe_forty + (self.nu - 40) * 0.03

    def sixty_tenth(self):
        return self.ten + self.ten_twe + self.twe_forty + self.forty_sixty + (
            self.nu - 60) * 0.015

    def over_ten(self):
        return self.ten + self.ten_twe + self.twe_forty + self.forty_sixty + self.sixty_tens + (
            self.nu - 100) * 0.001


def calculation():
    while True:
        try:
            nu = int(input('Please input your monthly profit(ten thousand): '))
        except ValueError:
            print('please input number!!')
        else:
            jjq = Jjq(nu)
            if nu <= 10:
                return jjq.under_ten()
            elif nu > 10 and nu < 20:
                return jjq.ten_twen()
            elif nu > 20 and nu < 40:
                return jjq.twen_forty()
            elif nu > 40 and nu < 60:
                return jjq.four_sixty()
            elif nu > 60 and nu < 100:
                return jjq.sixty_ten()
            elif nu > 100:
                return jjq.over_ten()
            else:
                print('error')


print(str(calculation() * 10000) + '￥')


# # 字典排序

# In[15]:


"""
利用字典的值对字典进行排序,将{1:2,3:4,4:3,2:1,0:0}
按照字典的值从大到小进行排序
"""
number = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for j in sorted(number,reverse=True, key=lambda z : number[z]):
    print(str(j) + ' : ' + str(number.get(j)))


# # 两段代码输出测试

# In[1]:


# 第一段代码:
a = 1
def fun(a):
    a = 2
fun(a)
print(a)
# 输出结果为1
# 可以这么改
# a = 1
# def fun(a):
#     a = 2
#     return a
# print(fun(a))
# print(a)

# 第二段代码
a = []
def fun(a):
    a.append(1)
fun(a)
print(a)
# 输出结果为[1]


# # 另两段代码输出

# In[3]:


# 第一段:
class Person:
    name = 'aaa'
p1 = Person()
p2 = Person()
p1.name = 'bbb'
print(p1.name)
print(p2.name)
print(Person.name)

# 第二段:
class Person1:
    name = []
p3 = Person1()
p4 = Person1()
p3.name.append(1)
print(p3.name)
print(p4.name)
print(Person1.name)


# #  4个数字排列组合3位数

# In[5]:


"""有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？"""
for i in range(1, 5):
    # 第一位数
    for j in range(1, 5):
        # 第二位数
        for k in range(1, 5):
            # 第三位数
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)


# # 推算完全平方数

# In[6]:


"""一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？"""
import math
for i in range(10000):
    # 在10000之内寻找
    a = int(math.sqrt(i + 100))
    # i + 100能开方
    b = int(math.sqrt(i + 268))
    # i + 268能开方
    if (a * a == i + 100) and (b *b == i + 268):
        print(i)


# # 判断一年某一天

# In[26]:


"""输入某年某月某日，判断这一天是这一年的第几天？"""
year = int(input('input year: '))
month = int(input('input month: '))
day = int(input('input day: '))
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum1 = 0
if month <= 12 and month >= 1:
    for i in range(month-1):
        sum1 += months[i]
    if year % 4 == 0:
        sum1 += 1
    sum2 = sum1 + day       
else:
    print('please input month in 1-12 !!')
print('the day is ' + str(sum2))


# # 多个数字比大小

# In[7]:


"""输入三个整数x,y,z，请把这三个数由小到大输出"""
# -*- coding:utf-8 -*-
list1 = []
num = int(input('输入多少个数字作比较: '))
for j in range(num):
    list1.append(int(input('请输入第' + str((j + 1)) + '个数: ')))
list1.sort()
print(list1)


# # 斐波那契数列

# In[24]:


"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""
nu_dict = {'a0': 0, 'a1': 1}
for i in range(0, 9):
    nu_dict['a' +
            str(i + 2)] = nu_dict['a' + str(i)] + nu_dict['a' + str(i + 1)]
for key, value in nu_dict.items():
    print(value, end=' ')
print('\n')

# 第二种方法
def fib(n):
    a, b = 0, 1
    print(a)
    for i in range(n):
        a, b = b, a + b
        print(a)


fib(10)


# In[ ]:




