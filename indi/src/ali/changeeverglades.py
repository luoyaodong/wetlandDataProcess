import mysqlConnector


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
        elif count == 1:
            if result[2]=='LA':
                cur.execute("update plant set PopularEName=%s where ScientificName=%s",(result[1],result[0]))
            elif result[2]=='CH':
                cur.execute("update plant set PopularCName=%s where ScientificName=%s",(result[1],result[0]))
    conn.commit()
    cur.close
    conn.close

def changePlantLevel():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("update plant left JOIN  plantrank on  Plant.PlantRankID=plantrank.RankID set Level = plantrank.ChineseName")
    conn.commit()
    cur.close()
    conn.close()

def findRemotesensing():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from remotesensing ")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def addToEverglades(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        cur.execute("insert into everglades(Term,Property,Value,ThesauName) VALUE (%s,%s,%s,%s)",(result[1],result[2],result[3],result[4]))
    conn.commit()
    cur.close()
    conn.close()

def update(str):
    return

if __name__=="__main__":
    #extract()
    #updateName(addName())
    #changePlantLevel()
    addToEverglades(findRemotesensing())