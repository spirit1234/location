
magicicans = ['alice', 'david' ,'carolina']
for mag in magicicans:
	print(mag)
	print(magicicans)
	for aa in mag:
		print('aa:' + aa)

magicianss = ['alice', 'david', 'carolina']
for magician in magicianss:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
