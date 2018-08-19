#coding:utf-8

import mysqlConnector

def findStr(str,newstr):
    conn = mysqlConnector.getRemoteConn()
    cur = conn.cursor()
    cur.execute("select Id,Value from everglades WHERE Value =%s",(str,))
    results = cur.fetchall()
    for result in results:
        print result
        cur.execute("update everglades set Value = %s where Id=%s",(newstr,result[0]))
    conn.commit()
    cur.close()
    conn.close()
def addStr(str):
    conn = mysqlConnector.getRemoteConn()
    cur = conn.cursor()
    cur.execute("select Id,Value,Term from everglades1 WHERE Property=%s and Value=%s",('BT',str))
    results = cur.fetchall()
    for result in results:
        if result == None:
            continue
        else:
            cur.execute("insert into everglades1 (Term,Property,Value,ThesauName) VALUES(%s,%s,%s,%s)",(result[2],'SC','REMOTESENSING','Remotesensing'))
    conn.commit()
    cur.close()
    conn.close()

def addSC():
    conn = mysqlConnector.getRemoteConn()
    cur = conn.cursor()
    cur.execute("select Id,Value,Term from everglades1 WHERE Property=%s and ThesauName=%s", ('BT', 'Remotesensing'))
    results = cur.fetchall()
    for result in results:
        if result == None:
            continue
        else:
            cur.execute("insert into everglades1 (Term,Property,Value,ThesauName) VALUES(%s,%s,%s,%s)",
                        (result[2], 'SC', 'REMOTESENSING', 'Remotesensing'))
    conn.commit()
    cur.close()
    conn.close()


if __name__=="__main__":
    # addStr('Remote sensing data processing and method')
    # addStr('Remote Sensing Characteristic Parameters and Application')
    # addStr('Satellites and sensors')
    # addStr('Aeronautical remote sensing and sensors')
    # addStr('Remote Sensing Characteristic Parameters and Application/Remote sensing concept')
    # addStr('Remote sensing data and products')
    # addStr('Remote sensing data processing and method/Satellites and sensors')

    addSC()

    # findStr("遥感数据处理与方法","Remote sensing data processing and method")
    # findStr("遥感特征参数与应用","Remote Sensing Characteristic Parameters and Application")
    # findStr("卫星及传感器","Satellites and sensors")
    # findStr("航空遥感及传感器","Aeronautical remote sensing and sensors")
    # findStr("遥感特征参数与应用/遥感领域概念","Remote Sensing Characteristic Parameters and Application/Remote sensing concept")
    #findStr("遥感数据及产品","Remote sensing data and products")
    # findStr("遥感数据处理与方法/卫星及传感器","Remote sensing data processing and method/Satellites and sensors")