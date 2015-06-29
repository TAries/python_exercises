#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''未做有效性验证
输入一个大于0小于100的数：99
一共9个，其中 3个25，2个10，0个5，4个1
'''


a=input('输入一个大于0小于100的数：')
b,c,d,e=0,0,0,0
b,bb=a/25,a%25
if bb>0:
    c,cc=bb/10,bb%10
    if cc>0:
        d,dd=cc/5,cc%5
        if dd>0:
            e=dd
mincoin=b+c+d+e
print '一共%d个，其中'%mincoin,
print '%d个25，%d个10，%d个5，%d个1'%(b,c,d,e)
