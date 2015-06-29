#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

'''

from random import randint,choice
lst,sublst=[],[]
N=randint(2,100)
N2=randint(1,100)

#生成列表lst，大小由N决定，元素由随机决定
for n1 in range(N):
    lst.append(randint(0,2**32-1))
print lst

#生成列表sublst，大小由N2决定，元素从lst中随机抽取
for n2 in range(N2):
    index=choice(lst)
    sublst.append(index)
#    lst.remove(index)

#排序，输出
sublst.sort()
print sublst
