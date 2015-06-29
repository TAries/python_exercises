#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
输入一个字符串: 12345678901234567890
输入要查找的字符：1
查找的字符首次出现在第1位置
查找的字符最后出现在第11位置
'''

def findchr():
    string=raw_input('输入一个字符串: ')
    char=raw_input("输入要查找的字符：")
    #正向和反向查找的标记
    ffind,bfind=0,0
    #正向和反向查找结果的位置
    findex,bindex=0,0

    #正向查找
    for n in range(len(string)):
        if string[n]==char:
            ffind=1
            findex= n
            break
        else:pass
    if ffind==1:
        print '查找的字符首次出现在第%d位置'%(findex+1)
    else:
        print '未找到！！！'

    #反向查找
    for n in range(len(string)-1,-1,-1):
        if string[n]==char:
            bfind=1
            bindex=n
            break
        else:pass
    if bfind==1:
        print '查找的字符最后出现在第%d位置'%(bindex+1)
    else:
        print 'weizhaodao'


if __name__=='__main__':
    findchr()
            
            

