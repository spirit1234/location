# -*- coding:utf-8 -*-
def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# 调用多次
describe_pet('dog', 'qiuqiu')
# 为了防止位置写错可以采用关键字实参调用
describe_pet(pet_name='lucky', animal_type='poodle')
