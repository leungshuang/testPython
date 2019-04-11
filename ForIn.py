#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# for in 迭代
from collections.abc import Iterable


def test_for_in():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d)
    for key in d:
        print(key)
        print(d.get(key))

    for word in 'ABC':
        print(word)


test_for_in()


# 判断是否可迭代 通过collections模块的Iterable类型判断 from collections import Iterable
def test_for_in2():
    a = isinstance('abc', Iterable)  # str是否可迭代
    b = isinstance([1, 2, 3], Iterable)
    c = isinstance(123, Iterable)
    print(a, b, c)


test_for_in2()


# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：


def for_emun():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)


for_emun()


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def find_min_and_max(l):
    min_num = l[0]
    max_num = l[0]
    if isinstance(l, Iterable):
        for value in l:
            if value < min_num:
                min_num = value
            elif value >= max_num:
                max_num = value
    r = (min_num, max_num)
    print(r)
    return (min_num, max_num)


lst = [3, 4, 56, 1, 2, 23, 45, 121314, 1232, 45, 2]
find_min_and_max(lst)