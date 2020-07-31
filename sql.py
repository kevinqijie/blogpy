from pymysql import *
#python中调用pymysql

class Mysqlpython:
    def __init__(self,database='test',
                 host="localhost",
                 user="root",
                 password="",
                 port=3306,
                 charset="utf8"):#初始化里面参数
        self.host = host
        self.user =user
        self.password = password
        self.port = port
        self.charset = charset
        self.database = database

    def open(self):
        self.db = connect(host=self.host,
                          user=self.user,
                          port=self.port,
                          database=self.database,
                          password=self.password,
                          charset=self.charset)#连接数据库
        self.cur = self.db.cursor()#创建游标对象

    def close(self):
        self.cur.close()#关闭游标对象
        self.db.close()#关闭数据库连接

    def zhixing(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)#操作游标对象
            self.db.commit()#提交
            print("ok")
        except Exception as e:
            self.db.rollback()#事务回滚
            print("Failed",e)
        self.close()

    def all(self,sql,L=[]):
        try:
            self.open()
            self.cur.execute(sql,L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed",e)
        self.close()
