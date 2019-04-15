#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 高阶函数  就是让函数的参数能够接收别的函数
from functools import reduce


def add1(x, y, f):
    return f(x) + f(y)


def test():
    x = 10
    y = -22
    return add1(x, y, abs)


print(test())


# map()和reduce()函数


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


def map_f(x):
    return x * x


def map_run():
    l_param = range(1, 11)
    lst = list(map(map_f, l_param))
    print(lst)


map_run()


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add2(x, y):
    return x + x * y


def run_reduce():
    lst = range(1, 6)
    return reduce(add2, lst)


print(run_reduce())


# str转int
def str2int(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))


print(str2int('10'))


# 上述用lambda函数进一步简化成：


def char2num_2(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int_2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num_2, s))


print(str2int_2('122'))
