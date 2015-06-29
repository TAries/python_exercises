#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input a string :35543
your input string is 35543:
input a number :54353
your input string is 54353:

input a string :5345
your input string is 5345:
input a number :435t
input error !!!
'''


astring=raw_input('input a string :')
print 'your input string is %s:'%astring

aint=raw_input('input a number :')
try:
    aint=int(aint)
    print 'your input string is %d:'%aint
except Exception:
    print 'input error !!!'


