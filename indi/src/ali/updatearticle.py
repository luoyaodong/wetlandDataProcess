# -*- coding: UTF-8 -*-
import mysqlConnector

#选择AAID和authors
def findauthors():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute("select AAID,AU from 6W湿地文献")
    results = cur.fetchall()
    print results
    cur.close()
    conn.close()
    return results

def updateauthors(results):
    conn  = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count = cur.execute("select * from article where ID=%s ",(result[0]))
        if count !=0:
            cur.execute("update article set Authors=%s where ID=%s",(result[1],result[0]))
        else:
            continue
    conn.commit()
    cur.close()
    conn.close()

if __name__=='__main__':
    #findauthors()
    updateauthors(findauthors())