# -*- coding:utf-8 -*-

def isprime(n):
    if n<=2:
        print 'prime'
    else:
        i=n/2
        while i>1:
            if n%i==0:
                break            
            i-=1
        if i==1:
            print 'prime'
        else :
            print 'no prime,max factor is %d'%i

if __name__=='__main__':
    isprime(1)
    isprime(2)
    isprime(3)
    isprime(4)
    isprime(5)
    isprime(25)
