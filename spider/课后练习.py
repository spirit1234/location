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

