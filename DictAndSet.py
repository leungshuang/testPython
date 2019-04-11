#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Dict ，类似java的map,key-value模式


def dict_test():
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])
    print(d.get('Michael'))
    d.pop('Michael')
    print(d)


dict_test()


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。，例如


def set_test():
    s = set([1, 2, 3, 1, 2, 3])
    print(s)
    s.add('4')
    print(s)
    s.remove(3)
    print(s)
    s.remove('4')
    print(s)
    s.add(1)
    print(s)

    s1 = {1, 2, 3}
    print(s1)
    s2 = {2, 3, 4}
    print(s2)
    print(s1 & s2)
    print(s1 | s2)


set_test()


def test_sort():

    s3 = [3, 1, 2, 54, 6]
    print(s3)
    s3.sort()
    print(s3)


test_sort()


def test_set2():

    s = set('test')
    print(s)


test_set2()


def test_replace():
    a = 'abc'
    b = a.replace('a', 'A')
    print(b)


test_replace()
