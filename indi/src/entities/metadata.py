#coding:utf-8
import mysqlConnector

def getMetadata():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select Id,Title,Abstract,Keywords_authors,Keywords_Plus,Combined_Keywords_Phrases from 2497文献元数据')
    results = cur.fetchall()
    cur.close()
    cur.close()
    return results
