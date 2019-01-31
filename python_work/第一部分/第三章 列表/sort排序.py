#-*- coding:utf-8 -*-
cars = ['bmw' ,'audi', 'toyota' , 'subaru']
cars.sort(reverse=True)
#reverse：相反 也就是反向排序  False就是正向排序
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere id the oriinal list again:")
print(cars)
