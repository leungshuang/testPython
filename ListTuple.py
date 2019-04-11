#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#list和tuple
#list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates,'长度：',len(classmates))
print(classmates,'长度（用+连接只能接str类型字符，否则报错）：'+str(len(classmates)))
print(classmates[1])
print(classmates[-1])
classmates.insert(0, 'JJ')
print(classmates)
classmates.insert(1, 'JJ2')
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[4])
print(classmates[-1])
print(classmates[-5])
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
classmates.insert(-2,'Leung')
print(classmates)
classmates.insert(-3,'222')
print(classmates)
classmates.append('ss')
print(classmates)

#tuple：元组。和list非常类似，但是tuple一旦初始化就不能修改
t1=(1,2,3)

t2=(1) #定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t3 = (1,)

print(t1,t2,t3)

t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'c'
t[2][1] = 'd'
print(t)