#coding:utf-8
import databaseConnect


def findDescription():
    conn = databaseConnect.getConn()
    cur = conn.cursor()
    count = cur.execute('select 序号,拉丁文名称 from 中国湿地动物物种_汇总')
    results = cur.fetchall()
    cur.close()
    conn.close()
    # for result in results:
    #     print result[7]
    return results

def findAnimalDescription():
    conn = databaseConnect.getWetlandConn()
    cur = conn.cursor()
    count = cur.execute('select ScientificName,ID from animal')
    results = cur.fetchall()
    cur.close()
    conn.close()
    # for result in results:
    #     print result[7]
    return results



def findDupDescription():
    conn = databaseConnect.getConn()
    cur = conn.cursor()
    count = cur.execute('select 拉丁文 from 中国湿地动物生物分类_定稿')
    results = cur.fetchall()
    cur.close()
    conn.close()
    # for result in results:
    #     print result[7]
    return results


def findAnimalDescriptionFromWetland():
    conn = databaseConnect.getWetlandConn()
    cur = conn.cursor()
    cur.execute('select ScientificName,ID from animal')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def updateAnimal(list1,list2):
    num =0
    count = 1010
    for m in list1:
        for n in list2:
            if(m[0]==n[0]):
                conn = databaseConnect.getWetlandConn()
                cur = conn.cursor()
                cur.execute('update animal_copy1 set ID=%s where ScientificName=%s',(count,n[0]))
                conn.commit()
                cur.close()
                conn.close()
                count = count+1
                num = num +1
            else:
                continue

    print ("update animal id process complete,the count is:")
    print (num)
    print (count)

def findAnimal_copyDescription():
    conn = databaseConnect.getWetlandConn()
    cur = conn.cursor()
    cur.execute('select ScientificName,ID from animal_copy1')
    results = cur.fetchall()
    cur.close()
    conn.close()
    # for result in results:
    #     print result[7]
    return results

def updateAnimal(results):
    conn = databaseConnect.getWetlandConn()
    cur = conn.cursor()
    for result in results:
        print (result[0])
        cur.execute('update animal_copy1 set ScientificName=%s where ID=%s',(reg(result[0]),result[1]))
    conn.commit()
    cur.close()
    conn.close()
import re
def reg(s):
    return re.sub(r'\（.*\）','',s)
    #return re.sub(r'\(.*\)','',s)

if __name__=="__main__":
    #updateAnimal(findAnimalDescription(),findDupDescription())
    #updateAnimal(findAnimal_copyDescription())
    #print(reg("Rynchopiade（Skimmers）"))
    print(reg("Rynchopiade（Skimmers）"))