#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
输入需要显示行数：10
第1行： this is a line
第2行： this is another line
第3行： hello
第4行： this is still a line
第5行： world
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
    r=int(raw_input('输入需要显示行数：'))
    f=open('temp.txt')
    i=0 
    for eachline in f:            
        if i<r:
            i+=1
            print '第%d行： %s'%(i,eachline),
        else:
            pass
    f.close()
    os.remove('temp.txt')
#存在就直接读取
else:
    r=int(raw_input('输入需要显示的行数：'))
    f=open('temp.txt')
    i=0

    for eachline in f:            
        if i<r:
            i+=1
            print '第%d行： %s'%(i,eachline),
        else:
            pass
    f.close()
    
    os.remove('temp.txt')
    
