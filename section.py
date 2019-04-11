#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 切片


def section_test():
    lst = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(lst[0:3])  # lst[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
    print(lst[:3])  # 如果第一个索引是0，还可以省略
    print(lst[-2:])  # 它同样支持倒数切片
    print(lst[-4:-1])  # 记住倒数第一个元素的索引是-1，若写上-1，包左不包右，所以-1不显示,-4会显示
    print(lst[-4:5])
    print(lst[2:3])


section_test()


def section_test2():
    l2 = list(range(1, 101))
    print(l2)
    l3 = l2[10:20]
    print(l3)
    l4 = l2[10:20:2]  # 在11-20个数之间，每隔两个取一次数
    print(l4)
    print(l2[::5])  # l2所有数据，隔五取一


section_test2()


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：


def tuple_section():
    lt = (0, 1, 2, 3, 4, 5)
    print(lt[:3])


tuple_section()
