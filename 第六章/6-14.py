#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
（1）剪刀
（2）石头
（3）布
输入你的选择：3
你出的是布
我出的是剪刀
我赢了
'''

def Rochambeau():
    a=raw_input('''
（1）剪刀
（2）石头
（3）布
输入你的选择：''')
    
    if a=='1':
        a=1
        print '你出的是剪刀'
    elif a=='2':
        a=2
        print '你出的是石头'
    elif a=='3':
        a=4
        print '你出的是布'
    else:
        print 'ERROR!!!'
        import sys
        sys.exit()
    #随机
    from random import choice
    b=choice([1,2,4])
    if b==1:
        print '我出的是剪刀'
    elif b==2:
        print '我出的是石头'
    elif b==4:
        print '我出的是布'
    #判断
    if a==b:
        print '平手！！！'
    elif a<b:
        if b-a<3:
            print '我赢了'
        else:
            print '你赢了'
    else:
        if a-b<3:
            print '你赢了'
        else:
            print '我赢了'
    


if __name__=='__main__':
    Rochambeau()
            
            

