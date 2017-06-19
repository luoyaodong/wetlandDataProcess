#coding:utf-8
import MySQLdb

def getConn():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='123',
            db ='neo4j',
            charset='utf8'
            )
    return conn
def getGeoConn():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='123',
            db ='db_test',
            charset='utf8'
            )
    return conn

def getJulyConn():
    conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user='root',
        passwd='123',
        db ='July',
        charset='utf8'
        )
    return conn

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")


