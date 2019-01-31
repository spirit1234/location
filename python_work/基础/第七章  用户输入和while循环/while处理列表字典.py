# -*- coding-utf-8 -*-
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()
    print('Verifying user: ' + confirmed_user.title())
    confirmed_users.append(confirmed_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素
letter = ['a', 'b', 'e', 'c', 'd', 'e', 'f', 'g']
print(letter)
while 'e' in letter:
    letter.remove('e')
print(letter)
# 如果把while变成if将只减少一个e

# 使用用户输入填充字典(现实生活中的调查)
responses = {}
polling_active = True
while polling_active:
    name = input('What\'s your name? ')
    response = input('How old are you? ')
    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(str(name) + ' \'s age is ' + str(response) + ' years old')
