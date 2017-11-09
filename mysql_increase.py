#coding:utf-8
import sys
import MySQLdb
class Transfermoney(object):
    def __init__(self,conn):
        self.conn = conn
    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from allmsan where acctid =%s"%acctid
            cursor.execute(sql)
            print "check-id:"+sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" % acctid)
        finally:
            cursor.close()


    def has_enough_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from allmsan where acctid =%s and money>%s" % (acctid,money)
            cursor.execute(sql)
            print "has_enough_money:"+ sql
            rs = cursor.fetchall()#把结果集放在变量里面，判断结果集条数（select）
            if len(rs) != 1:
                raise Exception("账号%没有足够的钱" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update allmsan set money=money-%s where acctid=%s" % (money,acctid)
            cursor.execute(sql)
            print "reduce_money:" + sql
            if cursor.rowcount != 1:#表示这条sql语句堵数据库产生多少影响（update）
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update allmsan set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print "add_money:" + sql
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cursor.close()


#使用参数输入来验证
# 设置的地方：
#
# Run/Debug Configurations->Configurations->Script Parames
#
# 和vs类似，都不用输入程序名字，直接输入参数即可。
#
# 如，在命令行中需要输入 python a.py b c d
#
# 则在上述地方直接输入 b c d就行了
if __name__=="__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    conn = MySQLdb.connect(host = "127.0.0.1",user ="root",passwd = "",db = "account")
    tr_money = Transfermoney(conn)
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "出现问题"+str(e)
    finally:
        conn.close()