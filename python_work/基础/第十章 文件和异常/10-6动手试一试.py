# -*- coding:utf-8 -*-
""" 加法运算 ： 提示用户提供数值输入时， 常出现的一个问题是， 用户提供的是文本而不是数字。 在这种情况下，
当你尝试将输入转换为整数时， 将引发TypeError 异常。 编写一个程序， 提示用户输入两个数字， 再将它们相加并打印结果。
在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。 对你编写的程序进行测试： 先输入两个数字，
 再输入一些文本而不是数字。"""

"""编写的代码放在一个while 循环中， 让用户犯错（输入的是文本而不是数字） 后能够继续输入数字。"""


def sum_nu():
    bol = True
    while bol:
        try:
            num1 = int(input("Write a number: "))
            num2 = int(input("Write another number: "))
        except ValueError:
            print("Please write number, however, not a word")
        else:
            sum = num1 + num2
            return sum


print(sum_nu())
