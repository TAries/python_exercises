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
a={'d':400,'e':500,'a':100,'b':200,'c':300}
b=[]
for n in a.keys():
    b.append(n)
b.sort()
print b
for n in b:
    print 'a[{0}] : {1}'.format(n,a[n])
