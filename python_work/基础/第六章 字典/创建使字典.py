# -*- coding:utf-8 -*-
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

'''先创建空字典的方式'''
alien_1 = {}
alien_1['color'] = 'red'
alien_1['point'] = 10
print(alien_1)

'''修改字典中的值'''
alien_0['color'] = 'blue'
print(alien_0)

'''移动位置跟踪示例'''
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置增量：
alien_3['x_position'] += x_increment
print('New x_position:' + str(alien_3['x_position']))

''' 删除一个键值对
    原始的alien_1'''
print(alien_1)
# 删除后的
del alien_1['color']
print(alien_1)
