#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#循环
def testCycle():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
      print(name)

testCycle()

print(list(range(1,101)))


def testGaosiSum():
    sum = 0
    for i in range(1,101):
        sum += i
    print(sum)

testGaosiSum()

#while循环
#阶乘法一：递归
def fact1(n):
    if(n==1):
        return 1;
    return n*fact1(n-1)

print(fact1(5))

#阶乘法二：循环
def fact2(n):
    result = 1;
    while(n>=1):
        if(n==1):
            print(result)
        result *= n
        n -= 1

fact2(6)