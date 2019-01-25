# -*- coding:utf-8 -*-
"""OrderedDict 实例的行为几乎与字典相同， 区别只在于记录了键—值对的添加顺序。"""
from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()
favorite_languages['a'] = 'python'
favorite_languages['b'] = 'java'
favorite_languages['c'] = 'php'
favorite_languages['d'] = 'c++'
for name, language in favorite_languages.items():
    print(name + '\'s favorite language is ' + language)

print(randint(1, 5))
