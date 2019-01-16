# -*- coding-utf-8 -*-
'''熟食店:创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字;再创建一个名为finished_sandwiches的空列表。
遍历列表sandwich_orders ， 对于其中的每种三明治， 都打印一条消息，如I made your tuna sandwich ，
并将其移到列表finished_sandwiches 。 所有三明治都制作好后， 打印一条消息， 将这些三明治列出来。'''
sandwich_orders = ['Arepa', 'Doner Kebab', 'Smoked Meat']
finished_sandwiches = []
for i in sandwich_orders:
    print('I made your %s sandwich' % i)
    finished_sandwiches.append(i)
print('making...')
for j in finished_sandwiches:
    print('%s sandwich finished' % j)

'''梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world,
 where would you go?”的提示， 并编写一个打印调查结果的代码块。'''
places = {}
judge = True
while judge:
    name = input('Please input your name: ')
    place = input('If you could visit one place in the world,where would you go?: ')
    places[name] = place
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        judge = False
for name, place in places.items():
    print('%s wants to visit %s' % (name, place))
