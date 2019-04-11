#!/usr/bin/env python 
# -*- coding:utf-8 -*-
a=abs(123)
b=abs(-123)
c=max(1,3,5,7,-10,19,2)
d=int(12.34)
e=int('12')
f=str(100)
g=bool(1)
h=bool(0)
i=bool('')
j=bool(22)
k=abs
print(a,b,c,d,e,f,g,h,i,j,k(-12210))

#--unicode转换 ord：字符->Unicode编码，chr：Unicode编码->字符
print(ord('A'))
print(ord('梁'))
print(chr(26970))
print(chr(70))
print('十六进制编码:','\u4e2d\u6587')

#字节类型：要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('梁爽'.encode('utf-8'))
print('梁爽'.encode('gbk'))
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe6\xa2\x81\xe7\x88\xbd'.decode('utf-8'))
print(b'\xe6\xa2\x81\xe7\x88\xbd'.decode('gbk'))
print(b'\xc1\xba\xcb\xac'.decode('gbk'))