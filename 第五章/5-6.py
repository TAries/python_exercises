#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
输入一个算术表达式：4321**3
第一个操作数是：4321，
第二个操作数是：3，
操作符是：**，
表达式运算结果为：80677568161
'''

import sys
a=raw_input('输入一个算术表达式：')
if '+' in a:
    op='+'
elif '-' in a:
    op='-'
elif '**' in a:#优先判断**，避免和*混淆
    op='**'
elif '/' in a:
    op='/'
elif '%' in a:
    op='%'
elif '*' in a:
    op='*'
else:
    print 'ERROR!!!'
    sys.exit()
n=a.split(op)
try:
    n1,n2=int(n[0]),int(n[1])
except:
    print 'ERROR,BYE !!!'
    sys.exit()
if op=='+':
    result=n1+n2
elif op=='-':
    result=n1-n2
elif op=='*':
    result=n1*n2
elif op=='/':
    result=n1/n2
elif op=='%':
    result=n1%n2
elif op=='**':
    result=n1**n2
print '''第一个操作数是：{0}，
第二个操作数是：{1}，
操作符是：{2}，
表达式运算结果为：{3}'''.format(n1,n2,op,result)
