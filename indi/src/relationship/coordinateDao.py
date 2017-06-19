# -*- coding: UTF-8 -*-
import math
import nltk
import re
import coordinateDaoImpl
import coordinateRegular
import types



import convention

#对湿地公约的数据进行提取

def extractCoordinate():
    results = convention.findDescription()
    for result in results:
        if result != None:
            coordinate = result[2]
            if coordinate!= None:
                co=coordinateRegular.coordinateRegularExtract(coordinate.split(' '))
                coordinateRegular.coordinateStandard(co)
                coordinateDaoImpl.insertCoordinate(result[0],result[1],co)
            else:
                continue
        else:
            continue
#对湿地公约的数据进行标准化
def extractStandard():
    results = convention.findStandard()
    for result in results:
        if result != None:
            coordinate = result[2]
            if coordinate!=None:
                #print coordinate
                if coordinateRegular.regular(coordinate):
                    coordinateDaoImpl.insertIntoStandard(result[1],result[6],coordinate)
                else:
                    coordinateDaoImpl.insertIntoExcept(result[1],result[6],coordinate)
            else:
                continue
        else:
            continue


def convertTo(latitude,):
    la=[]

    if latitude<0:
        la.append('-')
        latitude=-latitude

    la.append(int(latitude))
    la.append('°')

    la.append(int((latitude-int(latitude))*60))
    la.append('′')

    la.append(int(((latitude-int(latitude))*60-int((latitude-int(latitude))*60))*60))
    la.append('″')

    la2=''
    for l in la:
        if type(l)==type(1):
            s=str(l)
            la2=la2+s
        else:la2=la2+l
    return la2

def convertToLo(longitude):
    lo=[]

    if longitude<0:
        lo.append('-')
        longitude=-longitude

    lo.append(int(longitude))
    lo.append('°')

    lo.append(int((longitude-int(longitude))*60))
    lo.append('′')

    lo.append(int(((longitude-int(longitude))*60-int((longitude-int(longitude))*60))*60))
    lo.append('″')
    la2=''
    lo2=''

    for o in lo:
        if type(o)==type(o):
            s=str(o)
            lo2=lo2+s
        else:lo2=lo2+o
    print lo2
    return lo2

if __name__=="__main__":
    extractStandard()
