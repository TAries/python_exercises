# -*- coding:utf-8 -*-
'''
'''
#返回n的因子，因子之积等于n
def getfactors(n):
    a=[1]
    i=2
    while i<n+1:
        while n%i==0:
            a.append(i)
            n/=i
        else:
            i+=1
    return a

def isperfect(n):
    a=getfactors(n)
    if sum(a)==n:
        return 1
    else:
        return 0

      
if __name__=='__main__':
    print isperfect(6)
    print isperfect(39)
    
