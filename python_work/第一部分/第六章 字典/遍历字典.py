# -*- coding:utf-8 -*-
alien = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'A'
}
# 遍历字典
for key, value in alien.items():
    print(str(key) + ': ' + str(value))
# 遍历字典中所有的键(按顺序)
for i in sorted(alien.keys()):
    print(i)
# 便利字典中所有的值(按顺序且剔除重复的值set函数)
for j in sorted(set((alien.values()))):
    print(j)
