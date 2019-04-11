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
