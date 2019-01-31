# -*- coding:utf-8 -*-
"""查看自己生日是否在圆周率的前100万中"""
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    contents = file_object.readlines()
    pi_string = ''
    for i in contents:
        pi_string += i.rstrip().replace(" ", '')
    """打印圆周率前52位"""
    print(pi_string[:52] + '...')
    print(len(pi_string))
    file_str = input('input your birth month and day, for example 19980101 or 0101\nplease input: ')
    count = 0
    for i in range(len(pi_string) - len(file_str)):
        i += 1
        j = i + len(file_str)
        abc = ''
        for nu in pi_string[i:j]:
            abc += nu
        count += 1
        if file_str in abc:
            print('In ' + str(count) + ' place, this position have birthday in pi digits')
        else:
            continue
    if file_str not in pi_string:
        print('sorry, have not find your birthday in pi million digits')

# word = ''
# word += nu
# d += 1
# if word in 'ghij':
#     print('d' + str(d))
# else:
#     print('none')

# abcd = 'abcdefghijk'
# ab = ''
# for i in abcd[:4]:
#     ab += i
# print(ab)
