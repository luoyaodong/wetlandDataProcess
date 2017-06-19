#coding:utf-8
import plantsRelationDaoImpl


def findPlantRelation(names,results):
    for des in results:
        if des[6] == None:
            continue
        for name in names:
            if name == None:
                continue
            if name in des[6]:
                plantsRelationDaoImpl.add(name,des[6], des[0], des[1],);
            else:
                continue

def findSynonymName(names,results):
    for des in results:
        if des[6] == None:
            continue
        for name in names:
            if name[3] == None:
                continue
            list = name[3].split(',')
            for l in list:
                l = extractBracket(l)
                l = extractDot(l)
                if l == '':
                    continue
                if l == None:
                    continue
                if l ==  ' L.':
                    continue
                if l in des[6]:
                    #写入拉丁名,异名,description,wetland_id,wetland_name到表中
                    plantsRelationDaoImpl.addSynonymName(name[1],l,des[6],des[0],des[1])
                else:
                    continue

            else:
                continue
def findSynonymNameToLiterature(names,results):
    for des in results:
        if des == None:
            continue
        for name in names:
            if name[3] == None:
                continue
            list = name[3].split(',')
            for l in list:
                l = extractBracket(l)
                l = extractDot(l)
                if l == '':
                    continue
                if l == None:
                    continue
                if l ==  ' L.':
                    continue
                for d in des:
                    if isNum(d):
                        continue
                    if d==None:
                        continue
                    if l in d:
                        #写入拉丁名,异名,description,wetland_id,wetland_name到表中
                        plantsRelationDaoImpl.addSynonymNameToLiterature(name[1],l,d,des[0],des[1])
                    else:
                        continue

            else:
                continue
def findSynonymNameToMetadata(names,results):
    for des in results:
        if des == None:
            continue
        for name in names:
            if name[3] == None:
                continue
            list = name[3].split(',')
            for l in list:
                l = extractBracket(l)
                l = extractDot(l)
                if l == '':
                    continue
                if l == None:
                    continue
                if l ==  ' L.':
                    continue
                for d in des:
                    if isNum(d):
                        continue
                    if l in d:
                        #写入拉丁名,异名,description,wetland_id,wetland_name到表中
                        plantsRelationDaoImpl.addSynonymNameToMetadata(name[1],l,d,des[0],des[1])
                    else:
                        continue

            else:
                continue

def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True
#去除.号后面的字符
def extractDot(str):
    try:
        newlist = []
        list = str.split(' ')
        for l in list:
            if l == '':
                continue
            if l == None:
                continue
            if l.find('.')!=-1:
                return ' '.join(newlist)
            else:
                newlist.append(l)
    except ValueError:
        return str
def extractBracket(str):
    try:
        pos = str.index(' (')
        return str[:pos]
    except ValueError:
        return str


if __name__ == '__main__':
    print  extractBracket('Panicum purpurascens Raddi,Panicum barbinode Trin.,Brachiaria purpurascens (Raddi) Henrard,Urochloa mutica (Forssk.) T. G. Nguyen,Panicum muticum Forssk.')
