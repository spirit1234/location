
players = ['a','b','c','d','e','f']
print(players[0:3])
print(players[-4:])

#遍历切片

for i in players[0:3]:
	print(i)
	
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('hamba')
friend_foods.append('apple')
print('after my_food')
print(my_foods)
print('\n after friend_foods')
print(friend_foods)
