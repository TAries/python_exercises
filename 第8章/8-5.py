# -*- coding:utf-8 -*-
'''
[1]
[1, 2]
[1, 2, 2, 3, 5]
[1, 2, 2, 2, 3, 5]
[1, 67]
'''
def getfactors(n):
    '''
判断方法：
依次判断从1到n的某数是否是n的因子，如果是，将因子加到结果列表里
并将n变为除去该因子后的数，继续判断
如果不是，则判断下一个
'''
    a=[1]
    i=2
    while i<n+1:
        while n%i==0:
            a.append(i)
            n/=i
        else:
            i+=1
    print a

if __name__=='__main__':
    getfactors(1)
    getfactors(2)
    getfactors(60)
    getfactors(120)
    getfactors(67)
