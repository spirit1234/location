# -*- coding:utf-8 -*-
# 有时候， 需要将一系列字典存储在列表中， 或将列表作为值存储在字典中， 这称为嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 复杂版
aliens = [alien_0, alien_1, alien_2]
for i in aliens:
    print(i)
# 简化版(适用于多个变量)
'''aliens = ['alien_'+str(i) for i in range(0,3)]
for j in aliens:
    print(locals()[j])'''

# 创建30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for i in aliens[:5]:
    print(i)
print('...')
print("aliens number is: " + str(len(aliens)))

# 随着游戏进行改变外星人颜色、速度等
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 遍历前五个
for alien in aliens[:5]:
    print(alien)

# 字典中存储列表
# 存储pizza信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print('you orderd a ' + pizza['crust'] + '-crust pizza' + 'with the follows toppings')
for topping in pizza['toppings']:
    print('\t' + topping)

# 最喜欢的语言，调查者不一定只回答一个最爱
favorite_languages = {
    'a': ['python', 'vb'],
    'b': ['c'],
    'c': ['php', 'go'],
    'd': ['python', 'java']
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name + '\'s favorite languages is ')
    else:
        print('\n' + name + ' \'s favorite language are ')
    for language in languages:
        print(language)

# 每位用户存储三项信息:名、 姓和居住地；利用字典嵌套字典的方式
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
# 进行遍历字典
for username, user_info in users.items():
    print('\n' + 'Username: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('Full name: ' + full_name.title() + '\n' + 'Location in ' + location.title())
