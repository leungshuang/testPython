#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回


def lazy_sum(*args):
    def sum_test():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum_test


def run():
    r = lazy_sum(1, 3, 5, 7, 9)
    print(r)  # 返回的函数并没有立刻执行
    print(r())  # 而是直到调用了f()才执行


run()


# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：


def test_equal():
    f1 = lazy_sum(1, 2, 3, 4, 5)
    f2 = lazy_sum(1, 2, 3, 4, 5)
    print(f1 == f2)


test_equal()


# 结论：f1()和f2()的调用结果互不影响


# 闭包


def count_test():
    fsx = []
    for i in range(1, 4):
        def fxx():
            return i*i
        fsx.append(fxx)
    return fsx


fr = count_test()
print(fr())
