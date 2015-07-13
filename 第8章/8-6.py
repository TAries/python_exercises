# -*- coding:utf-8 -*-
'''getfactors()已经实现了返回素数因子的功能
'''
#返回n的因子，因子之积等于n
def getfactors(n):
    a=[]
    i=2
    while i<n+1:
        while n%i==0:
            a.append(i)
            n/=i
        else:
            i+=1
    return a

#判断n是否为素数
def isprime(n):
    if n<=2:
        return True
    else:
        i=n/2
        while i>1:
            if n%i==0:
                break            
            i-=1
        if i==1:
            return True
        else :
            return False


def primefactor(n):
    b=[]
    a=getfactors(n)
    for i in a:
        if isprime(i):
            b.append(i)
    return b

      
if __name__=='__main__':
    print getfactors(27)
    print primefactor(539)
    
