#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
while 0--10 : 0 1 2 3 4 5 6 7 8 9 10 
for 0--10 : 0 1 2 3 4 5 6 7 8 9 10
'''


a=0
print 'while 0--10 :',
while a<=10:
    print a,
    a+=1

print '\nfor 0--10 :',
for aa in range(0,11):
    print aa,
