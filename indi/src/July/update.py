#coding=utf8
import mysqlConnector
import wetlandconvention

information = wetlandconvention.information_all()

def updateNameAndLocation():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    results = wetlandconvention.getmessycode()
    print results
    count = 0
    for result in results:
        count = count+1
        cur.execute("update 湿地公约_copy set 湿地名称=%s,地理坐标=%s where 湿地编码=%s",(result[0],result[1],result[2]))
    print count
    conn.commit()
    cur.close()
    conn.close()
def updateMessyCode3():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    results = wetlandconvention.getmessycode3()
    print results
    for result in results:
        cur.execute("update 湿地公约_copy set 总体生态特征=%s where 湿地编码=%s",(result[0],result[1]))
    conn.commit()
    cur.close()
    conn.close()
def updateByInformation_all():
    conn = mysqlConnector.getJulyConn()
    cur = conn.cursor()
    results = information.getInformation_all()
    for result in results:
        T = (result[0],result[1],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],
             result[13],result[14],result[2])
        #   print T
        fetchnumber = cur.execute("select * from 湿地公约_copy where 湿地编码=%s",(result[2],))
        #print result[2]
        if fetchnumber == 1:
            cur.execute("update 湿地公约_copy set 湿地名称=%s,国家=%s,面积=%s,指定日期=%s,地理坐标=%s,概述=%s,国家行政区域=%s,国家法定名称=%s"
                        ",区域性国家法律名称=%s,最后出版日期=%s,以前版本链接=%s,RIS文件链接=%s,位置地图链接=%s,GIS文件链接=%s where 湿地编码=%s",T)
        if fetchnumber == 0:
            cur.execute("insert into 湿地公约_copy(湿地名称,国家,面积,指定日期,地理坐标,概述,国家行政区域,国家法定名称,区域性国家法律名称,最后出版日期,以前版本链接,RIS文件链接,位置地图链接,GIS文件链接,湿地编码) "
                        "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",T)
    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    #updateNameAndLocation()
    #updateMessyCode3()
    updateByInformation_all()
