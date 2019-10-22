import MySQLdb

def getConn():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='123',
            db ='neo4j',
            charset='utf8'
            )
    return conn


def getWetlandConn():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='123',
            db ='wetland',
            charset='utf8'
            )
    return conn