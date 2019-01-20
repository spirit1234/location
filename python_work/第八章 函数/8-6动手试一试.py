# -*- coding-utf-8 -*-
'''城市名：编写一个名为city_country() 的函数， 它接受城市的名称及其所属的国家。至少使用三个城市-国家对调用这个函数， 并打印它返回的值。'''


def city_country(city, country):
    full = city + ', ' + country
    return full


print('"%s"' % (city_country('Beijing', 'China')))
print('"%s"' % (city_country('Shanghai', 'China')))
print('"%s"' % (city_country('New York', 'American')))

'''专辑：编写一个名为make_album() 的函数， 它创建一个描述音乐专辑的字典。 这个函数应接受歌手的名字和专辑名，
并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。'''


def make_album(singer_name, album_name):
    music = {
        'singer': singer_name,
        'album': album_name
    }
    return music


musician = make_album('zhengyuan', 'baorong')
print(musician)

'''编写一个while 循环， 让用户输入一个专辑的歌手和名称。 获取这些信息后， 使用它们来调用函
数make_album() ， 并将创建的字典打印出来。 在这个while 循环中， 务必要提供退出途径。'''
print('\nenter q to exit')
while True:
    sin = input('input a singer name: ')
    if sin == 'q':
        break
    alb = input('input this singer\'s album name: ')
    if alb == 'q':
        break
    information = make_album(sin, alb)
    print(information)
