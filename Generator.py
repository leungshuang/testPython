#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# generator创建 方法一：


def gen_test():
    lst = (x * x for x in range(1, 11))
    print(lst)
    print(next(lst), next(lst), next(lst))  # next可以获取generator下一个元素，但是基本不用
    for x in (x * x for x in range(1, 11)):  # 一般用for in 循环获取
        print(x)


gen_test()

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
#
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：


def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

# 注意，赋值语句：a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# 但不必显式写出临时变量t就可以赋值


fib(10)


def fib2(max_num):  # 等价于fib()的函数：
    n = 0
    a = 0
    b = 1
    while n < max_num:
        print(b)
        t = a + b
        a = b
        b = t
        n += 1
    return 'done'


fib2(10)
