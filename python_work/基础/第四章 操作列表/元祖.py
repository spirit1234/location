
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#试验元祖不能改变值
#dimensions[0] = 230

#遍历元组里的值
for value in dimensions:
	print(value)

#虽然不能修改元组，但是可以重新定义赋值
dimensions = (400,100)
print("after modify:")
print(dimensions)
for value in dimensions:
	print(value)
