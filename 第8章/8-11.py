# -*- coding:utf-8 -*-
'''
一共有多少个人： t
一共有多少个人： 2
输入第1个人的英文名字： t,t
输入第2个人的英文名字： tt
输入的名字有误，必须是last，first格式 !!!
这是你第1次输错！！！
输入第2个人的英文名字： tt,
输入的名字有误，必须是last，first格式 !!!
这是你第2次输错！！！
输入第2个人的英文名字： a,a  
你输入的人名按字母排序为：
a,a
t,t
'''

while 1:
    try:
        name_count=int(raw_input('一共有多少个人： ').strip())
        break
    except:
        pass
namelist=[]
i_name=1
error_time=0
while i_name<=name_count:
    name=raw_input('输入第%d个人的英文名字： '%i_name).strip().strip(',')
    if not (name.find(',')and name.count(',')==1):
        print '输入的名字有误，必须是last，first格式 !!!'
        error_time+=1
        print '这是你第%d次输错！！！'%error_time
        continue
    else:
        namelist.append(name)
        i_name+=1

namelist.sort()
print '你输入的人名按字母排序为：'
for eachname in namelist:
    print eachname
        
        
    

    
    

            
