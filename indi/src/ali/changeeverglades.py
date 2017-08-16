import mysqlConnector
import re

def findSC():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from everglades where Property='SC'")
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results


def updateeverglades(result,id):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("update everglades set Value=%s where Id=%s",(result,id))
    conn.commit()
    cur.close()
    conn.close()
    pass


def replace(str):
    start = str.index(':')
    newstr = str[start+1:]
    bracket = newstr.index("(")
    newstr = newstr[:bracket]
    return newstr

def extract():
    results = findSC()
    for result in results:
        updateeverglades(replace(result[2]),result[4])


def addName():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from plantvername")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def updateName(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count = cur.execute("select * from plant where ScientificName=%s",(result[0],))
        if count == 0:
            continue
        if count == 1:
            cur.execute("update plant set PopularCName=%s,PopularEName=%s where ScientificName=%s",(result[1],result[2],result[0]))
    conn.commit()
    cur.close
    conn.close


def update(str):
    return

if __name__=="__main__":
    #extract()
    updateName(addName())