#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input 1st number :55
input 2nd number :455
input 3rd number :43
sorted : 43 55 455
'''

i=0
while i<3:
    while True:
        try:
            a=raw_input('input 1st number :')
            a=int(a)
            i+=1
            break
        except:
            print 'wrong input!!!'
    while True:
        try:
            b=raw_input('input 2nd number :')
            b=int(b)
            i+=1
            break
        except:
            print 'wrong input!!!'
    while True:
        try:
            c=raw_input('input 3rd number :')
            c=int(c)
            i+=1
            break
        except:
            print 'wrong input!!!'
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print 'sorted :',a,b,c

    


