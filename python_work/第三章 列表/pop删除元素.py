#-*- coding:utf-8 -*-
name = ['jing' , 'jian' , 'qiang']
print(name)
#方法pop() 可删除列表末尾的元素， 
#并让你能够接着使用它。 术语弹出 （pop） 
#源自这样的类比： 列表就像一个栈， 
#而删除列表末尾的元素相当于弹出栈顶元素。
name_new = name.pop()
print(name)
print(name_new)


motorcycles = ['honda' ,'yamaha' , 'suzuki']
last_owned = motorcycles.pop()

print("The last motorcycles I owned was a " + last_owned.title() +'.')
