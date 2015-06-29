#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''未做有效性验证
输入一个1-1000的数字：0
0

输入一个1-1000的数字：1
  one

输入一个1-1000的数字：999
nine hundred and ninety  nine

输入一个1-1000的数字：1000
输入数字不对！！！
'''


a=raw_input('输入一个1-1000的数字：')
inta=int(a)
inta100=inta/100#a除以100的商，即百位
inta100yu=inta%100#a除以100的余，即后两位
inta10=inta100yu/10#出去百位后除以10的商，即十位
inta10yu=inta100yu%10#出去百位后除以10的余，即个位
a=list(a)


#判断百位
if inta100>=0 and inta100<10:
    if inta100==0:
        inta100=''
    elif inta100==1:
        inta100='one hundred and '
    elif inta100==2:
        inta100='two hundred and'
    elif inta100==3:
        inta100='three hundred and'
    elif inta100==4:
        inta100='four hundred and'
    elif inta100==5:
        inta100='five hundred and'
    elif inta100==6:
        inta100='six hundred and'
    elif inta100==7:
        inta100='seven hundred and'
    elif inta100==8:
        inta100='eight hundred and'
    elif inta100==9:
        inta100='nine hundred and'
else:
    inta100='输入数字不对！！！'
    print inta100
    import sys
    sys.exit()

#判断十位
if inta10!=0:
    if inta10==1:
        pass
    elif inta10==2:
        inta10='twenty '
    elif inta10==3:
        inta10='thirty '
    elif inta10==4:
        inta10='forty '
    elif inta10==5:
        inta10='fifty '
    elif inta10==6:
        inta10='sixty '
    elif inta10==7:
        inta10='seventy '
    elif inta10==8:
        inta10='eighty '
    elif inta10==9:
        inta10='ninety '
else:inta10=''

#判断十位为1时的个位
if inta10==1:
    if inta10yu==0:
        inta10yu='ten'
    elif inta10yu==1:
        inta10yu='eleven'
    elif inta10yu==2:
        inta10yu='twelve'
    elif inta10yu==3:
        inta10yu='thirteen'
    elif inta10yu==4:
        inta10yu='fourteen'
    elif inta10yu==5:
        inta10yu='fifteen'
    elif inta10yu==6:
        inta10yu='sixteen'
    elif inta10yu==7:
        inta10yu='seventeen'
    elif inta10yu==8:
        inta10yu='eighteen'
    elif inta10yu==9:
        inta10yu='nineteen'
#判断十位不为1时的个位
else:
    if inta10yu==0:
        inta10yu=''
    elif inta10yu==1:
        inta10yu='one'
    elif inta10yu==2:
        inta10yu='two'
    elif inta10yu==3:
        inta10yu='three'
    elif inta10yu==4:
        inta10yu='four'
    elif inta10yu==5:
        inta10yu='five'
    elif inta10yu==6:
        inta10yu='six'
    elif inta10yu==7:
        inta10yu='teen'
    elif inta10yu==8:
        inta10yu='eight'
    elif inta10yu==9:
        inta10yu='nine'

if inta100=='' and inta10=='' and inta10yu=='':
    print 0
else:
    print inta100,inta10,inta10yu
