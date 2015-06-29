#!/usr/bin/python
#-*-coding:utf-8-*-
'''

'''


from datetime import datetime,timedelta
db={}
info={}
def newuser():
    prompt='login desired: '
    while True:
        #name不区分大小写
        name=raw_input(prompt).strip().lower()
        if not name.isalnum():
            prompt='name incorrect,try another: '
            continue
        if name in db.keys():
            prompt='name taken, try another: '
            continue
        else:
            break
    pwd=raw_input('passwd: ')
    #密码和最后登录时间
    info['password']=pwd
    info['last_login']=''
    db[name]=info

def olduser():
    name=raw_input('login: ')
    pwd=raw_input('passwd: ')
    try:
        #防止db引用不存在的键
        passwd=db[name]['password']
    except:
        print 'except,login incorrect'
    else:
        if passwd==pwd:
            print 'welcome back ',name
            last_time=db[name]['last_login']
            if last_time=='':
                print 'this is the first time you login!!!'
                last_time=datetime.now()
                db[name]['last_login']=last_time
            else:
                #last_login=db[name]['last_login']
                print 'Last time you login at :%s'%str(last_time)[:19]
                if datetime.now()-last_time<timedelta(1):
                    print 'login more than one time in one hour !!!'
        else:
            print 'login incorrect'
#显示所有用户
def showalluser():
    if len(db)==0:
        print 'have no user!!!'    
    else:
        for k in db.keys():
            print '{0} : {1}'.format(k,db[k]['password'])
#删除用户
def deleteuser():
    name=raw_input('enter a name you want to delete: ')
    if name not in db.keys():
        print 'no user named %s'%name
    else:
        del db[name]
        print 'del user named %s !!!'%name

def showmenu():
    prompt='''
(U)ser Login
(D)elete a User
(S)how all users
(Q)uit

Enter chioce: '''
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print '\nYou picked: [%s]'%choice
            if choice not in 'uqds':
                print 'invalid option ,try again'
            else :
                chosen=True
        if choice=='q':done=True
        if choice=='u':
            while True:
                choice=raw_input('are you a (O)ld user or a (N)ew one ?').strip().lower()
                if choice=='o':
                    olduser()
                    break
                elif choice=='n':
                    newuser()
                    break
                else:
                    print 'enter wrong !!!'
                             
        if choice=='s':showalluser()
        if choice=='d':deleteuser()

if __name__=='__main__':
    showmenu()
