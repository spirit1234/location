
'''计算1~1 000 000的总和 ： 创建一个列表， 其中包含数字1~1 000 000， 再使用min() 和max() 核实该列表确实是从1开始， 到1 000 000结束的。 
另外， 对这个列表调用函数sum() ， 看看Python将一百万个数字相加需要多长时间。计算1~1 000 000的总和 ： 创建一个列表， 其中包含数字1~1 000 000， 
再使用min() 和max() 核实该列表确实是从1开始， 到1 000 000结束的。 另外， 对这个列表调用函数sum() ， 看看Python将一百万个数字相加需要多长时间。'''
list1  =  list(range(1,1000000))
sum1 = sum(list1)
a = min(list1)
b = max(list1)
c = '到'
d = "%d%s%d"%(a,c,b)
print(d)
print(sum1)

'''通过给函数range() 指定第三个参数来创建一个列表， 其中包含1~20的奇数； 再使用一个for 循环将这些数字都打印出来。'''

list2 = list(range(1,20,2))
for i in list2:
	print(i)
print(list2)

'''3的倍数 ： 创建一个列表， 其中包含3~30内能被3整除的数字； 再使用一个for 循环将这个列表中的数字都打印出来。'''

list3 = list(range(3,30,3))
for j in list3:
	print(j)
print(list3)

'''将同一个数字乘三次称为立方。 例如， 在Python中， 2的立方用2**3 表示。 请创建一个列表， 其中包含前10个整数（即1~10） 的立方， 再使用一个for 循
环将这些立方数都打印出来。'''

list4 = []
for k in range(1,10):
	l = k**3
	list4.append(l)
	print(list4)
for t in list4:
	print(t)

list5 = []
for y in range(1,10):
	z = y**3
	if z in range(10):
		list5.append(z)
		print(z)
	else:
		break
print(list5)

'''立方解析 ： 使用列表解析生成一个列表， 其中包含前10个整数的立方。'''
list6 = [value**3 for value in range(1,10)]
print(list6)
