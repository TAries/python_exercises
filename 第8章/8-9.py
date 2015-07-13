# -*- coding:utf-8 -*-
'''
'''


def fib(N):
    if N<3:
        return 1
    else:
        a,b,=1,1
        n=2
        while n<N:
            a,b=b,a+b
            n+=1
        return b
print fib(8)
            
