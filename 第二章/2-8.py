#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
input a number :432
input a number :543
input a number :63
input a number :f
wrong input !!!
input a number :645
input a number :3
sum of numbers you input is 1686
list you input is : [432, 543, 63, 645, 3] and sum of it is 1686
'''

i,sum,sum2,l=0,0,0,[]
while i<5:
    try:
        a=raw_input('input a number :')
        a=int(a)
        sum+=a
        l.append(a)
        i+=1
    except:
        print 'wrong input !!!'
print 'sum of numbers you input is %d'%sum
for index in l:
    sum2+=index
print 'list you input is :',
print l,
print 'and sum of it is %d'%sum2
    


