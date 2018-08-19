import mysqlConnector


def findallwetland():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from information_all")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def updatewetland(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:

        count = cur.execute("select * from wetlandprotectarea where WetlandProtectAreaID=%s",(result[2]))
        if count == 1:
            cur.execute("update wetlandprotectarea set Administative_region=%s,National_legal_designation=%s,Country=%s where WetlandProtectAreaID=%s",(result[7],result[8],result[1],result[2]))
    conn.commit()
    cur.close()
    conn.close()

def findAllPapaerId():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select ID from article")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def change(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count1 = cur.execute("select * from articleanimal where ArticleID=%s",(result[0],))
        print count1
        count2 = cur.execute("select * from articleplant where ArticleID=%s",(result[0],))
        print count2
        count3 = cur.execute("select * from wetlandprotectareaarticle where ArticleID=%s",(result[0],))
        count = count1+count2+count3
        if count ==0:
            cur.execute("delete from article where ID=%s",(result[0],))
        else:
            continue
    conn.commit()
    cur.close()
    conn.close()

if __name__=="__main__":
    #updatewetland(findallwetland())
    #change(findAllPapaerId())
    change(findAllPapaerId())