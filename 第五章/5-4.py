#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

'''


a=input('输入一个年份：')
if (a%4==0 and a%100!=0) or (a%4==0 and a%100==0):
    print '闰年'
else:print '平年'
