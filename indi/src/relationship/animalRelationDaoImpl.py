import mysqlConnector
def addAnimalRelation(id, name, sciname, description,wetland_id,wetland_name):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    T = (id,name,sciname,description,'has',wetland_id,wetland_name)
    cur.execute('insert animalToWetland values(%s,%s,%s,%s,%s,%s,%s)',T)
    conn.commit()
    cur.close()
    conn.close()
    return None
