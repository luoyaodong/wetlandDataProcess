import mysqlConnector
def addRelation(geoname, wetland):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T=geoname+wetland
    count = cur.execute('select geonameid from geonameToWetland where geonameid=%s and wetland_id=%s',(geoname[0],wetland[0]))
    if count == 1:
        return
    elif count == 0:
        cur.execute('insert into geonameToWetland(geonameid,name,asciiname,alternatenames,latitude,longitude,wetland_id,'
                    'wetland_name,location) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',T)
    conn.commit()
    cur.close()
    conn.close()
    return None
