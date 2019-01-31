
'''打印消息“The first three items in the list are:”， 再使用切片来打印列表的前三个元素。'''
list1 = ['a','b','c','d','e','f','g','h','i','j','k']
print("The first three items in the list are")
print(list1[:3])
'''打印消息“Three items fromthe middle of the list are:”， 再使用切片来打印列表中间的三个元素。'''
length = len(list1)
ab = int(length/2-1)

print('Three items fromthe middle of the list are:')
print(list1[(ab):(ab+3)])

'''打印消息“The last three items in the list are:”， 再使用切片来打印列表末尾的三个元素。'''
print('The last three items in the list are:')
print(list1[-3:])

'''打印a-o不重复的遍历'''
list3 = []
list2 = ['a','h','i','j','k','l','m','n','o']
for i in list1:
	if i in list2:
		continue
	else:
		list3.append(i)
for k in list2:
	list3.append(k)
print(list3)

