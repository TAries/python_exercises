#!/usr/bin/python
#-*-coding:utf-8-*-
'''
aaa : 1
bbb : 2
ccc : 3
ddd : 4
[('aaa', 1), ('bbb', 2), ('ccc', 3), ('ddd', 4)]

'''



a={'aaa':1,'ddd':4,'bbb':2,'ccc':3}
b=[]
for k in a.keys():
    b.append(k)
b.sort()
for n in b:
    print '%s : %s'%(n,a[n])

#按值排序，d[0]为按键
d=sorted(a.iteritems(),key=lambda d:d[1])
print d


