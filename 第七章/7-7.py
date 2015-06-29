#!/usr/bin/python
#-*-coding:utf-8-*-
'''
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'd'} {'a': 1, 'c': 3, 'b': 2, 'd': 5}
'''


a={1:'a',2:'b',3:'c',4:'d',5:'d'}
b={}
for k,v in a.items():
    b[v]=k
print a,b
