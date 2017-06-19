# -*- coding: UTF-8 -*-
import mysqlConnector

def addRelation(AAID, title, wetland_id, wetland_name,description):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from literatureToWetland where AAID=%s and wetland_id=%s',(AAID,wetland_id))
    T=(AAID,title,wetland_id,wetland_name,description)
    S=(title,wetland_name,description,AAID,wetland_id,)
    if count == 1:
        cur.execute('update literatureToWetland set title=%s,wetland_name=%s,description=%s where AAID=%s and wetland_id=%s',S)
    elif count == 0:
        cur.execute('insert into literatureToWetland(AAID,title,wetland_id,wetland_name,description)values(%s,%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()


def getRelation():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select * from literatureToWetland ')
    cur.close()
    conn.close()
    return cur.fetchall()

def deleteRudundancyData():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('delete from literatureToWetland where wetland_name=%s or wetland_name=%s or wetland_name=%s',('Coll','Anda','PODA'))
    cur.close()
    conn.commit()
    conn.close()


def addPlantRelation(AAID, title, sci_name, w):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from literatureToPlant where AAID=%s and sci_name=%s',(AAID,sci_name))
    T=(AAID,title,sci_name,w)
    S=(w,title,AAID,sci_name)
    if count == 1:
        cur.execute('update literatureToPlant set description=%s where title=%s and AAID=%s and sci_name=%s',S)
    elif count == 0:
        cur.execute('insert into literatureToPlant(AAID,title,sci_name,description)values(%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()


def addAnimalRelation(AAID , title, sci_name, w):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from literatureToAnimal where AAID=%s and sci_name=%s',(AAID,sci_name))
    T=(AAID,title,sci_name,w)
    S=(w,title,AAID,sci_name)
    if count == 1:
        cur.execute('update literatureToAnimal set description=%s where title=%s and AAID=%s and sci_name=%s',S)
    elif count == 0:
        cur.execute('insert into literatureToAnimal(AAID,title,sci_name,description)values(%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()
