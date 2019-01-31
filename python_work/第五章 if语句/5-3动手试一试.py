
#假设在游戏中刚射杀了一个外星人， 请创建一个名为alien_color 的变量， 并将其设置为'green' 、 'yellow' 或'red' 。
alien_color = ('green','yellow','red')

#编写一条if 语句， 检查外星人是否是绿色的； 如果是， 就打印一条消息， 指出玩家获得了5个点。
ufo = 'green'
if ufo in alien_color[0]:
	print('you will have five point')
else:
	print('error')


'''如果外星人是绿色的， 就打印一条消息， 指出玩家因射杀该外星人获得了5个点。
如果外星人不是绿色的， 就打印一条消息， 指出玩家获得了10个点。'''

ufo = input('Please input the ufo\'s color: ')
if ufo in alien_color:
	if ufo in alien_color[0]:
		print('you will have five point')
	else:
		print('you will have ten point')
else:
	print('error')

'''如果外星人是绿色的， 就打印一条消息， 指出玩家获得了5个点。
如果外星人是黄色的， 就打印一条消息， 指出玩家获得了10个点。
如果外星人是红色的， 就打印一条消息， 指出玩家获得了15个点。'''
ufo = input('Please input the ufo\'s color: ')
if ufo in alien_color:
	if ufo in alien_color[0]:
		print('you will have five point')
	elif ufo in alien_color[1]:
		print('you will have ten point')
	else:
		print('you will have fifteen point')
else:
	print('error')

'''人生的不同阶段 ： 设置变量age 的值， 再编写一个if-elif-else 结构， 根据age 的值判断处于人生的哪个阶段。
如果一个人的年龄小于2岁， 就打印一条消息， 指出他是婴儿。
如果一个人的年龄为2（含） ～4岁， 就打印一条消息， 指出他正蹒跚学步。
如果一个人的年龄为4（含） ～13岁， 就打印一条消息， 指出他是儿童。
如果一个人的年龄为13（含） ～20岁， 就打印一条消息， 指出他是青少年。
如果一个人的年龄为20（含） ～65岁， 就打印一条消息， 指出他是成年人。
如果一个人的年龄超过65（含） 岁， 就打印一条消息， 指出他是老年人。'''
def err():
	try:
		age = int(input('Please input your age: '))
	except ValueError:
		err()
	else:
		if age in range(0,2):
			print('baby')
		elif age in range(2,4):
			print('study walk')
		elif age in range(4,13):
			print('child')
		elif age in range(13,20):
			print('teenagers')
		elif age in range(20,65):
			print('adult')
		else:
			print('old man')
err()
