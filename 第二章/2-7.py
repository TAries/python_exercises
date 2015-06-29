#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input a string :dsgdgdfg54353fdg
while --> d s g d g d f g 5 4 3 5 3 f d g
for --> d s g d g d f g 5 4 3 5 3 f d g
'''


a=raw_input('input a string :')
i=0
print 'while -->',
while i<len(a):
    print a[i],
    i+=1
print
print 'for -->',
for i in a:
    print i,
