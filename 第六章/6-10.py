#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
输入一个字符串，返回字母的大小写反转： ff4532GFDG
FF4532gfdg
'''

a=raw_input('输入一个字符串，返回字母的大小写反转: ')
if a=='':
    import sys
    sys.exit()
else:
    a=list(a)
    b=[]
    for n in a:
        if n.isupper():
            b.append(n.lower())
        elif n.islower():
            b.append(n.upper())
        else:
            b.append(n)
print ''.join(b)
            

