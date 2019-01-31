# -*- coding:utf-8 -*-
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''使用任意数量的关键字实参'''


def build_profile(first, last, **userinfo):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
