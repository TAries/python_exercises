#!/usr/bin/python
#-*-coding:utf-8-*-
'''
no match !!!
123fghgfasd

'''



def tr(srcstr,dststr,string):
    if srcstr in string:
        print string.replace(srcstr,dststr)
    else:
        print 'no match !!!'

if __name__=='__main__':
    tr('asd','dsf','ewrewtwfd')
    tr('asdd','123','asddfghgfasd')

