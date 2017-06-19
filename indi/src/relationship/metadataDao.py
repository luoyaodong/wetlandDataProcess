# -*- coding: UTF-8 -*-
import metadataDaoImpl


def findWetlandFromdatadata(datadata,wetlands):
    for data in datadata:
        if data == None:
            continue
        for wetland in wetlands:
            for d in data:
                if d == None:
                    continue
                if isNum(d):
                    continue
                if wetland[1] == None:
                    continue
                if wetland[1] in d:
                    metadataDaoImpl.addRelation(data[0],data[1],wetland[0],wetland[1],d)
# 判断是否为数字
def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True

def deleteData():
    metadataDaoImpl.deleteRudundancyData()

def findPlantFromdatadata(datadata,plants):
    for data in datadata:
        if data == None:
            continue
        for plant in plants:
            for w in data:
                if w == None:
                    continue
                if isNum(w):
                    continue
                if plant==None:
                    continue
                if plant in w:
                    metadataDaoImpl.addPlantRelation(data[0],data[1],plant,w)


def findAnimalFromdatadata(datadata, animals):
    for data in datadata:
        if data == None:
            continue
        for animal in animals:
            for w in data:
                if w == None:
                    continue
                if isNum(w):
                    continue
                if animal[3]==None:
                    continue
                if animal[3] in w:
                    metadataDaoImpl.addAnimalRelation(data[0],data[1],animal[3],w)
