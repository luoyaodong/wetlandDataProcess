#coding=utf-8
import mysqlConnector

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

def add(name,description,wetland_id,wetland_name):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T = (name,description,wetland_id,wetland_name,'has')
    #cur.execute('create table if not exists plantToWetland(id int, name varchar(255),description VARCHAR(255),relationship varchar(10))')
    cur.execute("insert into plantToWetland(name,description,relationship) values(%s,%s,%s,%d,%s)",T)
    conn.commit()
    cur.close()
    conn.close()


def addSynonymName(sciname, synname, description, wetland_id, wetland_name):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T = (sciname,synname,description,wetland_id,wetland_name)
    count = cur.execute('select * from plantSynToWetland where wetland_id=%s and sciname=%s',(wetland_id,sciname))
    if count == 1:
        return
    elif count ==0:
        cur.execute('insert into plantSynToWetland(sciname,synname,description,wetland_id,wetland_name) values(%s,%s,%s,%s,%s)',T)
    conn.commit()
    cur.close()
    conn.close()
    return None


def addSynonymNameToLiterature(sciname, synname, description, AAID, title):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T = (sciname,synname,description,AAID,title)
    count = cur.execute('select * from literatureToSynname where AAID=%s and sciname=%s',(AAID,sciname))
    if count == 1:
        return
    elif count == 0:
        cur.execute('insert into literatureToSynname(sciname,synname,description,AAID,title) values(%s,%s,%s,%s,%s)',T)
    conn.commit()
    cur.close()
    conn.close()
    return None

def addSynonymNameToMetadata(sciname, synname, description, metadata_id, title):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T = (sciname,synname,description,metadata_id,title)
    count = cur.execute('select * from metadataToSynname where metadata_id=%s and sciname=%s',(metadata_id,sciname))
    if count == 1:
        return
    elif count == 0:
        cur.execute('insert into metadataToSynname(sciname,synname,description,metadata_id,title) values(%s,%s,%s,%s,%s)',T)
    conn.commit()
    cur.close()
    conn.close()
    return None
