#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


def fn(n):
    return n % 2 == 1


def test_map(lst):
    return map(fn, lst)


print(list(test_map([2, 3, 4, 5])))


def test_filter(lst):
    return filter(fn, lst)


print(list(test_filter([2, 3, 4, 5])))


# 埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x : x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 练习 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def test_is_palindrome():
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))


test_is_palindrome()
