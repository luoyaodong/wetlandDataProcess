#coding=utf8
import mysqlConnector

def getmessycode():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    cur.execute("select * from 湿地公约乱码")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def getmessycode3():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    cur.execute("select * from 主表乱码3")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

class information_all():
    def getInformation_all(self):
        conn = mysqlConnector.getJulyConn()
        cur = conn.cursor()
        cur.execute("select * from information_all")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
