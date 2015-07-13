# -*- coding:utf-8 -*-
'''
输入一段英文，计算元音数： aeiou
5
'''


s=raw_input('输入一段英文，计算元音数： ')
s=''.join(s.split())
yuanyin=['a','e','i','o','u']
sum=0
for a in yuanyin:
    sum+=s.count(a)
print sum
    
    

            
