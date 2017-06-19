import coordinateDao
import  mysqlConnector
import time

def getGeoname():
    conn = mysqlConnector.getGeoConn()
    cur = conn.cursor()
    cur.execute('select geonameid,name,asciiname,alternatenames,latitude,longitude from do_table_copy')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def convertCoordinate(results):
    conn = mysqlConnector.getGeoConn()
    cur = conn.cursor()
    for coordinate in results:
        if coordinate==None:
            continue
        count = cur.execute('select geonameid from geoname where geonameid=%s',(coordinate[0],))
        if count==0:
            continue
        latitude = coordinateDao.convertTo(coordinate[4])
        longitude = coordinateDao.convertToLo(coordinate[5])
        # print latitude,longitude,coordinate[0]
        cur.execute('update geoname set latitude=%s,longitude=%s where geonameid=%s',(latitude,longitude,coordinate[0]))
        conn.commit()
    cur.close()
    conn.close()

if __name__=='__main__':
    now = time.strftime("%H:%M:%S")
    # getGeoname()
    convertCoordinate(getGeoname())
    end = time.strftime("%H:%M:%S")
    print (now+","+end)
