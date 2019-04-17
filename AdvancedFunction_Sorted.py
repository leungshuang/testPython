#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Python内置的sorted()函数就可以对list进行排序：


def fn1():
    return sorted([36, 5, -12, 9, -21])


print(fn1())


# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：


def fn2():
    return sorted([36, 5, -12, 9, -21], key=lambda x: abs(x))


print(fn2())


def fn3():
    return sorted(['bob', 'about', 'Zoo', 'Credit'])


print(fn3())


def fn4():
    return sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)


print(fn4())


# 假设我们用一组tuple表示学生名字和成绩：
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：


def by_name(lst):
    return lst[0]


def test_by_name():
    lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    lst2 = sorted(lst, key=by_name)
    print(lst2)


test_by_name()


# 合一写法


def test_by_name2():
    lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    lst2 = sorted(lst, key=lambda x: x[0])
    print(lst2)


test_by_name2()
