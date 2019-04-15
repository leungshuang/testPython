#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 高阶函数  就是让函数的参数能够接收别的函数


def add(x, y, f):
    return f(x) + f(y)


def test():
    x = 10
    y = -22
    return add(x, y, abs)


print(test())
