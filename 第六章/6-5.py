#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

'''


a=raw_input('输入一个字符串：')
a=list(a)
print a
aa=a[:]
aa.reverse()
print aa
aaa=a+aa
print aaa
b=''.join(aaa)
print '你输入的字符串形成的回文数是：%s'%b
