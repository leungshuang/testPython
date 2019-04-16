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


# 作业题：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# 自写


def normalize(name):
    return name.capitalize()


def first_upper(lst):
    return map(normalize, lst)


print(list(first_upper(['adam', 'LISA', 'barT'])))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# 自写


def prod(lst):
    return reduce(lambda x, y: x * y, lst)


print(prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


def digits_map(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def sp_lst(in_str):
    return in_str.split('.')


def int2str(int_in):
    return reduce(lambda x, y: x * 10 + y, map(digits_map, int_in))


def str2float(s):
    lst = sp_lst(s)
    int_in = int2str(lst[0])
    x_in = int2str(lst[1]) / (10 ** len(lst[1]))
    return int_in + x_in


print(str2float('123.456'))
