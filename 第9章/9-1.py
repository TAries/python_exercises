#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
***file contents:***
#this is a line
#this is another line
hello#my name is hahaha
#this is still a line
world 

***without # ***
hello
world
'''

import os

s1='''#this is a line
#this is another line
hello#my name is hahaha
#this is still a line
'''
s2='world'
#不存在就写入
if not os.path.exists('temp.txt'):
    f=open('temp.txt','w')
    f.write(s1)
    f.write(s2)
    f.close()
    print '***file contents:***'
    f=open('temp.txt')
    for eachline in f:
        print eachline,
    #剔除#以后的内容
    print '\n\n***without # ***'
    f.seek(0,0)
    for eachline in f:
        i=eachline.find('#')
        if i==-1:
            print eachline,
        elif i==0:
            pass
        else:
            eachline=eachline[0:i]
            print eachline

    f.close()
    os.remove('temp.txt')
#存在就直接读取
else:
    f=open('temp.txt')
    print '***file contents:***'
    for eachline in f:
        print eachline
#剔除#以后的内容
    print '\n***without # ***'
    f.seek(0,0)
    for eachline in f:
        i=eachline.find('#')
        if i==-1:
            print eachline,
        elif i==0:
            pass
        else:
            eachline=eachline[0:i]
            print eachline
    f.close()
    os.remove('temp.txt')
