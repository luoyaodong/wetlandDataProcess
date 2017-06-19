#coding:utf-8
import mysqlConnector


def findDescription():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select 湿地编码,湿地名称,地理坐标,大致位置,海拔,面积,植物区系,动物区系 from 湿地公约')
    results = cur.fetchall()
    cur.close()
    conn.close()
    #print results
    return results
def findLocation():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select 湿地编码,湿地名称,大致位置 from 湿地公约')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def findAll():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    results = cur.execute('select * from 湿地公约')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def findStandard():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select * from wetlandGeoFeatures')
    return cur.fetchall()
