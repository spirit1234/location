# -*- coding-utf-8 -*-
# 写一个1-100之间的猜数游戏
import random
a = int(random.random() * 100)
b = True
score = 100
print('Let\'s play a game, you input a integer number, and I\'ll tell you bigger or smaller')
while b:
    try:
        c = int(input('\nPlease input: '))
    except ValueError:
        print('Please input number!')
    else:
        if c > a:
            print('That\'s bigger')
            score -= 1
        elif c == a:
            print('So good, you are right')
            print('Your score: ' + str(score))
            print('\nWould you want another round?')
            d = input('Please input Yes/No: ')
            if d == 'Yes' or d == 'Yes'.lower() or d == 'Yes'.upper():
                b = True
                score = 100
            else:
                b = False
        else:
            score -= 1
            print('That\'s smaller')
