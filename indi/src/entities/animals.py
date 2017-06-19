#coding:utf-8
import MySQLdb

import mysqlConnector

def getAnimalSciName():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select 序号,动物名称,所属分类,拉丁文名称,英文名称,物种国内分布情况 from 中国湿地动物物种_汇总')
    result = cur.fetchall()
    return result
