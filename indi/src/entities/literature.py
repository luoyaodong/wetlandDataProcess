# -*- coding: UTF-8 -*-
import mysqlConnector

def getLiterature():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select AAID,TI,DE,ID,AB from 6W湿地文献')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
