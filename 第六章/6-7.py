#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''未做有效性验证
---剔除掉输入数字的因子---

enter a number: 20
BEFORE: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
AFTER: [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
'''


#输入一个数字字符串
num_str=raw_input('enter a number: ')

#将字符串转换为数字
num_num=int(num_str)

#生成一个1到输入数字的序列，并输出
fac_list=range(1,num_num+1)
print 'BEFORE:',fac_list

#变量i，初始化为0
i=0

#只要i小于输入的数字就循环
while i<len(fac_list):

    #如果num_num是fac_list值的整数倍，就标记fac_list对应的值
    if num_num %fac_list[i]==0:
        fac_list[i]=None
    #i加1
    i=i+1

#定义一个空的结果列表，如果fac_list的值未被标记，则将该值append到结果列表
r_list=[]
for n in range(0,len(fac_list)):
    if fac_list[n]!=None:
        r_list.append(fac_list[n])

#输出结果列表
print 'AFTER:',r_list
