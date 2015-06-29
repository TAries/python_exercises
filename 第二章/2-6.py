#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input a number :1
your input number is 1 ,and larger than 0
input a number :0
your input number is 0
input a number :-1000
your input number is -1000 ,and smaller than 0
input a number :g
wrong input !!!
'''


a=raw_input('input a number :')
try:
    a=int(a)
    if a>0:
        print 'your input number is %d ,and larger than 0'%a
    elif a==0:
        print 'your input number is 0'
    else:
        print 'your input number is %d ,and smaller than 0'%a
except:
    print 'wrong input !!!'
