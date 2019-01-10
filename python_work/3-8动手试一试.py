#-*- coding:utf-8 -*-
place = ['harbin' , 'jilin' ,'shenyang' , 'beijing' ,'shanghai']
print(place)

#使用sorted() 按字母顺序打印这个列表， 同时不要修改它。
order_place = sorted(place)
print(order_place)
print(place)

#使用sorted() 按与字母顺序相反的顺序打印这个列表， 同时不要修改它。
disorder_place = sorted(place,reverse=True)
print(disorder_place)
print(place)

#使用reverse() 修改列表元素的排列顺序。 打印该列表， 核实排列顺序确实变了。
change = place.reverse()
print(place)

#使用reverse() 再次修改列表元素的排列顺序。 打印该列表， 核实已恢复到原来的排列顺序。
dischange = place.reverse()
print(place)

#使用sort() 修改该列表， 使其元素按字母顺序排列。 打印该列表， 核实排列顺序确实变了。
tru = place.sort()
print(place)

#使用sort() 修改该列表， 使其元素按与字母顺序相反的顺序排列。 打印该列表， 核实排列顺序确实变了。
fal = place.sort(reverse=True)
print(place)

#使用len() 打印一条消息
print(len(place))
