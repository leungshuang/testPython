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


# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了


def fib3(num):
    n, a, b = 0, 0, 1
    print('fib3:')
    while n < num:
        yield b  # 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib3(10))  # 由于是generator


# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中


def fib4():
    g = fib3(10)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break


fib4()


def print_fib3():
    for value in fib3(10):
        print(value)


print_fib3()


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


# 练习
# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：


def triangles():
    p = [1]
    while True:
        yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]


def test_triangles(line_num):
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == line_num:
            break


test_triangles(1)
