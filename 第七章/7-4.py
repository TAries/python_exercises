#!/usr/bin/python
#-*-coding:utf-8-*-
'''
['a', 'b', 'c', 'd', 'e']
a[a] : 100
a[b] : 200
a[c] : 300
a[d] : 400
a[e] : 500
'''
a=[1,2,3,4,5,6,7,8,9,10]
b=['abc','def','ghi','jkl','mno','pqr','stu','vwx','yz0','123']
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
for k,v in c.items():
    print '{0} : {1}'.format(k,v)
