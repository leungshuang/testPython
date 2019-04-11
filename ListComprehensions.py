#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 列表生成式即List Comprehensions
import os


def list_comprehensions():
    lst = list(range(1, 11))
    print(lst)
    l2 = [x*x for x in lst]  # 列表生成式
    print(l2)
    # 筛选偶数的平方
    l3 = [x * x for x in lst if x % 2 == 0]
    print(l3)
    # 双循环组合
    x = ['A', 'B', 'C']
    y = ['X', 'Y', 'Z']
    l4 = [m + n for m in x for n in y]
    print(l4)


list_comprehensions()


# 列出目录 利用import os
def list_dir():
    dir_list = [d for d in os.listdir('E:\\360MoveData\\Users\\Administrator\\Desktop')]
    print(dir_list)


list_dir()


# 题目：如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# L = ['Hello', 'World', 18, 'Apple', None] 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
def practice():
    lst = ['Hello', 'World', 18, 'Apple', None]
    print(lst)
    r = [s.lower() for s in lst if isinstance(s, str)]
    print(r)


practice()
