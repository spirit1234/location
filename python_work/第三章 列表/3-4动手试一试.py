#-*- coding:utf-8 -*-
person = ['tong' , 'yang' ,'shen']
print(person)

fail_person = 'tong'
pass_person = 'jing'

person.remove(fail_person)
person.insert(0,pass_person)
print("tong is busy , so, " +pass_person+" instead him come")
for i in range(len(person)):
	print(person[i]+" please come")
	i += 1

print("Then we wwill have more people"+'\n')
people1 = 'chen'
people2 = 'zhang'
people3 = 'xin'

person.insert(0,people1)
person.insert(2,people2)
person.append(people3)

print(person)

print('because a little error , we have to let two people have dinner')
person.pop(0)
person.pop(2)
person.pop(3)
person.pop(1)
print("please "+person[0]+'、'+person[1]+" to have dinner!")

del person[1]
del person[0]
print(person)
