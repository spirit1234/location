# -*- coding-utf-8 -*-
# 写一个1-100之间的猜数游戏
import random
a = int(random.random() * 100)
b = True
print('Let\'s play a game, you input a integer number, and I\'ll tell you bigger or smaller')
while b:
    try:
        c = int(input('\nPlease input: '))
    except ValueError:
        print('Please input number!')
    else:
        if c > a:
            print('That\'s bigger')
        elif c == a:
            print('So good, you are right')
            print('\nWould you want another round?')
            d = input('Please input Yes/No: ')
            if d == 'Yes' or d == 'Yes'.lower() or d == 'Yes'.upper():
                b = True
            else:
                b = False
        else:
            print('That\'s smaller')
