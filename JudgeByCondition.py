#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#if 条件判断
def judgeAge(age):
    if 0<age<18:
        print('未成年')
    elif age<30:
        print('成年')
    elif age<50:
        print('中年')
    elif age >= 50:
        print('老年')
    else:
        print('年龄非法！')

judgeAge(1000)
12
#输入
def judgeAgeByInput():
    ageIn = input('请输入年龄：')
    age = int(ageIn)
    if 0<age<18:
        print('未成年')
    elif age<30:
        print('成年')
    elif age<50:
        print('中年')
    elif age >= 50:
        print('老年')
    else:
        print('年龄非法！')

judgeAgeByInput()