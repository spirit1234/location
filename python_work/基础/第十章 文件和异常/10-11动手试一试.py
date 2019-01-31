# -*- coding:utf-8 -*-
"""编写一个程序， 提示用户输入他喜欢的数字， 并使用json.dump() 将这个数字存储到文件中。 再编写一个程序，
从文件中读取这个值， 并打印消息“I know your favorite number! It's _____.”。"""
import json


def reader():
    filename = 'json/favorite_number.json'
    try:
        with open(filename) as file_obj:
            fav_nu = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_nu


"""以下注释是正确代码但有些瑕疵，当故意把int类型的input写成str型，如：我先输入'saf'，由于错误会进行create()函数重新调用，
第二次输入数字4会返回一个none值，而非数字4。这是因为return的特点，将函数结果返回，即退出create模块。
再次运行create()函数的时候，返回值会出现none的情况，但print(fav_num)还是有那个数值的。
"""

# def create():
#     try:
#         fav_num = int(input('Write your favorite number: '))
#     except ValueError:
#         create()
#     else:
#         filename = 'json/favorite_number.json'
#         with open(filename, 'w') as file_object:
#             json.dump(fav_num, file_object)
#             return fav_num
"""这个create方法改善了上面的瑕疵，采用while循环，从而避免重复调用create方法"""


def create():
    while True:
        try:
            fav_num = int(input('Write your favorite number: '))
        except ValueError:
            print('Please input number!!')
        else:
            filename = 'json/favorite_number.json'
            with open(filename, 'w') as file_object:
                json.dump(fav_num, file_object)
                return fav_num


def favorite():
    fav_nu = reader()
    if fav_nu:
        print('I know your favorite number! It\'s ' + str(fav_nu))
    else:
        num = create()
        print('Your favorite number ' + str(num) + ' has been remembered!')


favorite()
