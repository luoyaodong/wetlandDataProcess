# -*- coding: UTF-8 -*-
import literatureDaoImpl


def findWetlandFromLiterature(literature,wetlands):
    for liter in literature:
        if liter == None:
            continue
        for wetland in wetlands:
            for w in liter:
                if w == None:
                    continue
                if isNum(w):
                    continue
                if wetland[1] == None:
                    continue
                if wetland[1] in w:
                    literatureDaoImpl.addRelation(liter[0],liter[1],wetland[0],wetland[1],w)
# 判断是否为数字
def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True

def deleteData():
    literatureDaoImpl.deleteRudundancyData()

def findPlantFromLiterature(literature,plants):
    for liter in literature:
        if liter == None:
            continue
        for plant in plants:
            for w in liter:
                if w == None:
                    continue
                if isNum(w):
                    continue
                if plant==None:
                    continue
                if plant in w:
                    literatureDaoImpl.addPlantRelation(liter[0],liter[1],plant,w)


def findAnimalFromLiterature(literature, animals):
    for liter in literature:
        if liter == None:
            continue
        for animal in animals:
            for w in liter:
                if w == None:
                    continue
                if isNum(w):
                    continue
                if animal[3]==None:
                    continue
                if animal[3] in w:
                    literatureDaoImpl.addAnimalRelation(liter[0],liter[1],animal[3],w)
