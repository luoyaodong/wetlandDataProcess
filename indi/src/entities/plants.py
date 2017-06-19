#coding:utf-8
import MySQLdb

import mysqlConnector


def getPlantsSciName():
    conn=mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select Scientific_name from 中国植物志')
    print count
    results = cur.fetchall()
    name = []
    for r in results:
        for n in r:
            name.append(n)
    cur.close()
    conn.close()
    return name
def getPlantsSynonym():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select 物种名称,拉丁名_全称,别名,异名 from 中国湿地植物别名与异名')
    results = cur.fetchall()
    # print results
    return results

if __name__ == '__main__':
    getPlantsSynonym()
