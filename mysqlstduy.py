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
# cur.execute("CREATE TABLE if not EXISTS userinfo3(id int PRIMARY KEY AUTO_INCREMENT,username VARCHAR(255),passwd VARCHAR(255))")
cur.execute("insert into userinfo3(username,passwd) value('%s','%s')" %(username,passwod))#增加
cur.execute("update userinfo3 set passwd='123456'")#改
cur.execute("delete from userinfo3 where username='jrx'")#删
test.commit()#数据插入，修改，删除都要commit
cur.close()
test.close()

#提示输入用户名密码