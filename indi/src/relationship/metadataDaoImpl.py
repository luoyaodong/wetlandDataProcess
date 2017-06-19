import mysqlConnector


def addRelation(metadata_id, title, wetland_id, wetland_name, description):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from metadataToWetland where metadata_id=%s and wetland_id=%s',(metadata_id,wetland_id))
    T=(metadata_id,title,wetland_id,wetland_name,description)
    S=(title,wetland_name,description,metadata_id,wetland_id,)
    if count == 1:
        cur.execute('update metadataToWetland set title=%s,wetland_name=%s,description=%s where metadata_id=%s and wetland_id=%s',S)
    elif count == 0:
        cur.execute('insert into metadataToWetland(metadata_id,title,wetland_id,wetland_name,description)values(%s,%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()

def getRelation():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('select * from metadataToWetland ')
    cur.close()
    conn.close()
    return cur.fetchall()

def deleteRudundancyData():
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    cur.execute('delete from metadataToWetland where wetland_name=%s or wetland_name=%s or wetland_name=%s',('Coll','Anda','PODA'))
    cur.close()
    conn.commit()
    conn.close()


def addPlantRelation(metadata_id, title, sci_name, w):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from metadataToPlant where metadata_id=%s and sci_name=%s',(metadata_id,sci_name))
    T=(metadata_id,title,sci_name,w)
    S=(w,title,metadata_id,sci_name)
    if count == 1:
        cur.execute('update metadataToPlant set description=%s where title=%s and metadata_id=%s and sci_name=%s',S)
    elif count == 0:
        cur.execute('insert into metadataToPlant(metadata_id,title,sci_name,description)values(%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()


def addAnimalRelation(metadata_id , title, sci_name, w):
    conn = mysqlConnector.getConn()
    cur = conn.cursor()
    count = cur.execute('select * from metadataToAnimal where metadata_id=%s and sci_name=%s',(metadata_id,sci_name))
    T=(metadata_id,title,sci_name,w)
    S=(w,title,metadata_id,sci_name)
    if count == 1:
        cur.execute('update metadataToAnimal set description=%s where title=%s and metadata_id=%s and sci_name=%s',S)
    elif count == 0:
        cur.execute('insert into metadataToAnimal(metadata_id,title,sci_name,description)values(%s,%s,%s,%s)',T)
    cur.close()
    conn.commit()
    conn.close()
