# -*- coding:utf-8 -*-
__author__="jinglesing"
#1.环境搭建 MySQL数据库（5.5.6绿色版本）2.MySQLdb安装（MySQL-python-1.2.5.win32-py2.7.exe） 3.navicat安装 4.python语法基础（操作数据库）

import MySQLdb
test = MySQLdb.Connect(db='mysqlinfo1',host="127.0.0.1",user="root",passwd="")#链接数据库
cur = test.cursor()#生成游标
# cur.execute("show databases;")#返回所有结果
username = "jrx"
cur.execute("select * from userinfo where usrname='%s'"% username)
for data in cur.fetchall():
    print data

#创建一个表，用select查询
# CREATE TABLE if not EXISTS userinfo2(
# id int PRIMARY KEY AUTO_INCREMENT,
# username VARCHAR(255),
# passwd VARCHAR(255)
# )
username_jrx = 'jrx'
passwod = '123456'
#cur.execute("CREATE TABLE if not EXISTS userinfo3(id int PRIMARY KEY AUTO_INCREMENT,username VARCHAR(255),passwd VARCHAR(255))")
cur.execute("insert into userinfo3(username,passwd) value('%s','%s')" %(username,passwod))#增加
cur.execute("update userinfo3 set passwd='123456'")#改
#cur.execute("delete from userinfo3 where username='jrx'")#删
test.commit()#数据插入，修改，删除都要commit


#提示输入用户名密码,若用户名密码正确则提示验证成功，反之则失败
#1.提示输入用户名密码
#2.把用户名密码发到数据库核对

#raw_input()含有参数
username_one = raw_input(u"请输入用户名:".encode("utf-8"))
passwd_one = raw_input(u"请输入密码:".encode("utf-8"))
count = cur.execute("select * from userinfo3 where username='%s'and passwd='%s'"%(username_one,passwd_one))
results = cur.fetchone()
print "results=",results
print "count=",count
#count匹配数目 results None == Flase
if results:
    print u"验证成功"
    print u"修改密码"
    newpasswd = raw_input(u"请输入新密码:".encode("utf-8"))
    print "newpaasswd=",newpasswd
    try:
        cur.execute("update userinfo3 set passwd='%s'where username='%s'"%(newpasswd,username_one))
        test.commit()
        # thispasswood=""
        result = cur.execute("select * from userinfo3 where username='%s'"% username_one)
        result = cur.fetchone()
        print "result=",result
        thispasswood = result[2]
        print u'修改成，新密码是：%s'% thispasswood

    except:
        print u"修改出错"

else:
    print u'验证失败'
# if count:
#     print u"验证成功"
# else:
#     print u'验证失败'

cur.close()
test.close()


