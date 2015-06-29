#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input a number between 1 - 100 :1000
input a number between 1 - 100 :-100
input a number between 1 - 100 :-1
input a number between 1 - 100 :gfd
wrong input !!!
input a number between 1 - 100 :100
DONE !!!
'''

while True:
    a=raw_input('input a number between 1 - 100 :')
    try:
        a=int(a)
        if a in range(1,101):
            print 'DONE !!!'
            break
        else:
            pass
    except:
        print 'wrong input !!!'
    


