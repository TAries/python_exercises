#!/usr/bin/python
#-*-coding:utf-8-*-
'''
this program random two set named a and b ,
enter your guess about a&b : 1
guess incorrect!!!!!!!
enter your guess about a&b : 1
guess incorrect!!!!!!!
enter your guess about a&b : 1
guess incorrect!!!!!!!
set a is set([9, 2, 4, 6, 7])
set b is set([8, 1, 9, 7])
a & b is  set([9, 7])
a | b is  set([1, 2, 4, 6, 7, 8, 9])

'''



from random import randrange,randint

a=set()
b=set()
a_count=randint(1,10)
b_count=randint(1,10)
#随机生成set a和b
for i in range(a_count):
    a.add(randrange(0,10))
for i in range(b_count):
    b.add(randrange(0,10))

print 'this program random two set named a and b ,'

#最多猜错3次
n=0
while n<3:
    guessstr=raw_input('enter your guess about a&b : ')
    #输入的字符串用空格分开，并转换为数字型的set，输入非数字要报错，未处理
    guesslist=guessstr.split(' ')
    tempset=set(guesslist)
    guessset=set()
    for i in tempset:
        guessset.add(int(i))
    #判断
    if guessset==a&b:
        print 'guess correct!!!'
        break
    else :
        print 'guess incorrect!!!!!!!'
        n+=1
#猜错3次，给出答案
if n==3:
    print 'set a is %s'%a
    print 'set b is %s'%b
    print 'a & b is ',a&b
    print 'a | b is ',a|b

