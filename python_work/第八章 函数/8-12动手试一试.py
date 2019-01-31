# -*- coding:utf-8 -*-
'''三明治 ： 编写一个函数， 它接受顾客要在三明治中添加的一系列食材。 这个函数只有一个形参（它收集函数调用中提供的所有食材）
并打印一条消息， 对顾客点的三明治进行概述。 调用这个函数三次， 每次都提供不同数量的实参。'''


def make_pizza(*topping):
    print('adding ' + str(topping))


make_pizza('pork')
make_pizza('pork', 'chicken')
make_pizza('pork', 'chicken', 'beef')

'''汽车 ： 编写一个函数， 将一辆汽车的信息存储在一个字典中。 这个函数总是接受制造商和型号， 还接受任意数量的关键字实参。
这样调用这个函数： 提供必不可少的信息， 以及两个名称—值对， 如颜色和选装配件。'''


def make_car(made_in, produce, **info):
    car = {}
    car['made_in'] = made_in
    car['produce'] = produce
    for key, value in info.items():
        car[key] = value
    return car


car_info = make_car('China', 'outback', color='cyan', parts='Valve guide')
print(car_info)
