#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
文件一共5行
'''

import os

s1='''this is a line
this is another line
hello
this is still a line
'''
s2='world'
#不存在就写入
if not os.path.exists('temp.txt'):
    f=open('temp.txt','w')
    f.write(s1)
    f.write(s2)
    f.close()
    f=open('temp.txt')
    i=0 
    for eachline in f:
        i+=1
    print '文件一共%d行'%i
    f.close()
    os.remove('temp.txt')
#存在就直接读取
else:
    with open('temp.txt') as f:
        i=0
        for eachline in f:            
            i+=1
        print '文件一共%d行'%i
#    f.close()
    assert f.closed,'文件未关闭'
    os.remove('temp.txt')
    
