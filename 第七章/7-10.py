#!/usr/bin/python
#-*-coding:utf-8-*-
'''
enter string to rot13: AaBbCcDdEeXxYyZz123456.,;'';aaazzz
your string to en/decrypt was: AaBbCcDdEeXxYyZz123456.,;'';aaazzz
the rot13 string is: NnOoPpQqRrKkLlMm123456.,;'';nnnmmm

'''



def rot13():
    a=raw_input('enter string to rot13: ')
    b=''
    for n in a:
        if n.isalpha():
            if ord(n.lower())-ord('a')>=13:                
                b+=chr(ord(n)-13)
            else:                
                b+=chr(ord(n)+13)
        else:
            b+=n
    print 'your string to en/decrypt was: %s'%a
    print 'the rot13 string is: %s'%b

if __name__=='__main__':
    rot13()
