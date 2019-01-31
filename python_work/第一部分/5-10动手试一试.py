
''' 检查用户名 ： 按下面的说明编写一个程序， 模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表， 并将其命名为current_users 。'''

current_users = ['a','b','c','d','e','f','g','h','john']

#再创建一个包含5个用户名的列表， 将其命名为new_users ， 并确保其中有一两个用户名也包含在列表current_users 中。

new_users = ['a','b','t','y','i','w','q','JOHN']

'''遍历列表new_users ， 对于其中的每个用户名， 都检查它是否已被使用。 如果是这样， 就打印一条消息， 
指出需要输入别的用户名； 否则， 打印一条消息， 指
出这个用户名未被使用。'''

'''确保比较时不区分大消息； 换句话说， 如果用户名'John' 已被使用， 应拒绝用户名'JOHN' 。'''
for i in new_users:
	if i.upper() in current_users or i.lower() in current_users:
		print('please input other name, '+i+' could not use')
	else:
		print('you can use this name, '+i+' could use')

''' 序数 ： 序数表示位置， 如1st和2nd。 大多数序数都以th结尾， 只有1、 2和3例外。
在一个列表中存储数字1~9'''
count = list(range(1,10))
#遍历这个列表
#在循环中使用一个if-elif-else 结构， 以打印每个数字对应的序数。 输出内容应为1st 、 2nd 、 3rd 、 4th 、 5th 、 6th 、 7th 、 8th 和9th ， 但每个序
#数都独占一行
for i in count:
	if i == 1:
		print(str(i) + 'st')
	elif i == 2:
		print(str(i) + 'nd')
	elif i == 3:
		print(str(i) + 'rd')
	else:
		print(str(i) + 'th')

