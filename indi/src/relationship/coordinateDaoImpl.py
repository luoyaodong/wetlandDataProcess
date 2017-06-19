import mysqlConnector



def insertCoordinate(wetland_id,wetland_name,coordinate):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    S=(wetland_id,wetland_name,coordinate)
    count = cur.execute('select * from wetlandGeoFeatures where wetland_id=(%s)',(wetland_id,))
    if count == 1:
        T=(coordinate,wetland_id)
        cur.execute('update wetlandGeoFeatures set coordinate=%s where wetland_id=%s',T)
    elif count == 0:
        cur.execute('insert into wetlandGeoFeatures(wetland_id,wetland_name,coordinate) values(%s,%s,%s)',S)
    cur.close()
    conn.commit()
    conn.close()


def insertIntoStandard(wetland_id, wetland_name, coordinate):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    S=(wetland_id,wetland_name,coordinate)
    count = cur.execute('select * from wetlandGeoFeatures_copy where wetland_id=(%s)',(wetland_id,))
    if count == 1:
        T=(coordinate,wetland_id)
        cur.execute('update wetlandGeoFeatures_copy set coordinate=%s where wetland_id=%s',T)
    elif count == 0:
        cur.execute('insert into wetlandGeoFeatures_copy(wetland_id,wetland_name,coordinate) values(%s,%s,%s)',S)
    cur.close()
    conn.commit()
    conn.close()


def insertIntoExcept(wetland_id, wetland_name, coordinate):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    S=(wetland_id,wetland_name,coordinate)
    count = cur.execute('select * from wetlandGeoFeatures_copy1 where wetland_id=(%s)',(wetland_id,))
    if count == 1:
        T=(coordinate,wetland_id)
        cur.execute('update wetlandGeoFeatures_copy1 set coordinate=%s where wetland_id=%s',T)
    elif count == 0:
        cur.execute('insert into wetlandGeoFeatures_copy1(wetland_id,wetland_name,coordinate) values(%s,%s,%s)',S)
    cur.close()
    conn.commit()
    conn.close()
