import mysqlConnector
import re
import types

def findAuthorFromOrganization():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from organization")
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results

def updatePersonorganization(results):
    #print  type(results)
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count = cur.execute("select * from personorganization where OrganizationID=%s",(result[0]))
        if count != 0:
            cur.execute("update personorganization set OrganizationName=%s where OrganizationID=%s",(result[1],result[0]))
    conn.commit()
    cur.close()
    conn.close()

def findAuthorFromPersonorganization():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select RepAuthorID,CONCAT(GROUP_CONCAT(OrganizationName)) FROM personorganization GROUP BY RepAuthorID")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def updatePerson(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count = cur.execute("select * from person where AuthorID=%s",(result[0],))
        if count == 1:
            cur.execute("update person set Organization=%s where AuthorID=%s",(result[1],result[0]))
    conn.commit()
    cur.close()
    conn.close()

def findAuthorFromArticle():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("select * from article")
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results

def updateArticlePerson(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    for result in results:
        count = cur.execute("select * from ArticlePerson where ArticleID=%s",(result[0]))
        if count != 0:
            cur.execute("update ArticlePerson set title=%s where ArticleID=%s",(result[1],result[0]))
    conn.commit()
    cur.close()
    conn.close()

def findAuthorFromArticlePerson():
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor()
    cur.execute("SELECT AuthorID,CONCAT(GROUP_CONCAT(title)) FROM ArticlePerson GROUP BY AuthorID;")
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results

def updatePersonByPaper(results):
    conn = mysqlConnector.getMacLocalConn()
    cur = conn.cursor
    for result in results:
        count = cur.execute("select * from person where AuthorID=%s",(result[0],))
        if count == 1:
            cur.execute("update person set Paper=%s where AuthorID=%s",(result[1],result[0]))
    conn.commit()
    cur.close()
    conn.close()

if __name__=='__main__':
    #updatePersonorganization(findAuthorFromOrganization())
    #updatePerson(findAuthorFromPersonorganization())
    updateArticlePerson(findAuthorFromArticle())
    #updatePersonByPaper(findAuthorFromArticlePerson())
