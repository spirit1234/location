# -*- coding:utf-8 -*-
'''创建三个表示人的字典， 然后将这三个字典都存储在一个名为people 的列表中。
   遍历这个列表， 将其中每个人的所有信息都打印出来。 '''
person1 = {'name': 'a', 'age': 5}
person2 = {'name': 'b', 'age': 10}
person3 = {'name': 'c', 'age': 15}
people = [person1, person2, person3]
for i in people:
    print(str(i))
    for key, value in i.items():
        print(str(key) + ':' + str(value))

'''创建多个字典， 对于每个字典， 都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
 将这些字典存储在一个名为pets的列表中， 再遍历该列表， 并将宠物的所有信息都打印出来'''
a = {'type': 'cat', 'owner': 'jjq'}
b = {'type': 'dog', 'owner': 'tong'}
pets = [a, b]
for i in pets:
    print('\n')
    for key, value in i.items():
        print(str(key) + ': ' + str(value))

'''创建一个名为favorite_places 的字典。 在这个字典中， 将三个人的名字用作键； 
对于其中的每个人， 都存储他喜欢的1~3个地方。 遍历这个字典， 并将其中每个人的名字及其喜欢的地方打印出来。'''
favorite_places = {
    'z': {
        'place1': 'beijing',
        'place2': 'shanghai',
        'place3': 'suzhou'
    },
    'y': {
        'place1': 'Harbin',
        'place2': 'tianjin',
        'place3': 'changchun'
    },
    'x': {
        'place1': 'shenyang',
        'place2': 'taiwan',
        'place3': 'New York'
    }
}
for i, j in favorite_places.items():
    print('\n' + str(i) + ':')
    for key, value in j.items():
        print(str(key) + ' favorite place is ' + str(value))

'''创建一个名为cities 的字典， 其中将三个城市名用作键； 对于每座城市， 都创建一个字典，
 并在其中包含该城市所属的国家、 人口约数以及一个有关该城市的事实。 在表示每座城市的字典中， 
 应包含country 、 population 和fact 等键。 将每座城市的名字以及有关它们的信息都打印出来。'''
cities = {
    'Harbin': {
        'country': 'China',
        'population': '1093 ten thousand',
        'fact': 'Ice city'
    },
    'Beijing': {
        'country': 'China',
        'population': '2171 ten thousand',
        'fact': 'Capital'
    },
    'Shanghai': {
        'country': 'China',
        'population': '2418 ten thousand',
        'fact': 'Oriental Pearl Radio'
    }
}
for i, j in cities.items():
    print('\n' + str(i) + ' :')
    for key, value in j.items():
       print(str(key) + ' is ' + str(value))