# -*- coding:utf-8 -*-
favorite_languages = {
    'a': 'python',
    'b': 'java',
    'c': 'C',
    'd': 'C++',
    'e': 'php'
}

# 让键值对反转的方法：
inverse_dict = dict([val, key] for key, val in favorite_languages.items())
print(inverse_dict)
# 加键值对
fav = {
    'f': 'php',
    'g': 'python',
    'h': 'python',
    'i': 'java',
    'j': 'C',
    'k': 'python',
    'l': 'php',
    'm': 'php',
    'n': 'php'
}
favorite_languages.update(fav)
print(favorite_languages)
# 排序找出最受欢迎的语言(低配版)
a = 0
b = 0
c = 0
d = 0
e = 0
for i in favorite_languages.values():
    if i == 'python':
        a += 1
    elif i == 'java':
        b += 1
    elif i == 'C':
        c += 1
    elif i == 'C++':
        d += 1
    else:
        e += 1
print('python: ' + str(a))
print('java: ' + str(b))
print('C: ' + str(c))
print('C++: ' + str(d))
print('php: ' + str(e))
# 高级版
d = {}
# for循环遍历统计各个编程语言喜好的次数
for x in favorite_languages.values():
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(d)
# 对编程语言喜好次数的统计进行排序，从高到低
for i in sorted(d, reverse=True, key=lambda y: d[y]):
    print(str(i) + ': ' + str(d.get(i)))
