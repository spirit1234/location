
'''4岁以下免费；
4~18岁收费5美元；
18岁（含） 以上收费10美元。'''
def err():
	try :
		age = int(input("Please input your age : "))
	except ValueError:
		print("Please input the true age")
		err()
	else:
		if age in range(1,100) :
			if age < 4:
				print("Your admission cost is $0")
			elif age in range(4,18):
				print("Your admission cost is $5")
			else :
				print("Your admission cost is $10")
err()


	
