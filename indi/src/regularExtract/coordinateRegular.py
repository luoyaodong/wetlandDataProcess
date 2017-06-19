# -*- coding: UTF-8 -*-
import sys;
reload(sys)
sys.setdefaultencoding('utf-8')
import re

def coordinateRegularExtract(word):
    results = []
    for rep in word:
        if re.search(r'[0-9]',rep)!=None or re.search(r'^(W|E|S|N)',rep)!=None or re.search(r'(W|E|S|N)$',rep)!=None \
                or re.search(r'°|\'|"',rep)!=None:
            if re.search(r'^.*?[a-zA-Z]{2,}',rep)==None:
                results.append(replaceP(replaceQuestionMark(rep)))
        else:
            continue
    #print ' '.join(results)
    return ' '.join(results)


def coordinateStandard(word):
    results = []
    if re.search(r'°',word)!= None:
            print word
    for w in word:
        if isNumber(w):
            results.append(w)
        if isDegree(w):
            results.append(w)
        if isLongtitude(w):
            results.append(w)
        else:
            continue
    #print ''.join(results)
def isNumber(word):
    if re.search(r'[0-9]',word)!=None:
        return True
    else:
        return False

def isLongtitude(word):
    if re.search(r'W|E|S|N',word)!= None:
        return True
    else:
        return False

def isDegree(word):
    if re.search(r'°|\'|"',word)!= None:
        return True
    else:
        return False

def replaceQuestionMark(word):
    strinfo = re.compile(r'\?')
    w=strinfo.sub('°',word)
    return w
def replaceP(word):
    strinfo = re.compile(r'</p>|<p>')
    return strinfo.sub('',word)

def check(word):
    for rep in word:
        if re.search(r'[0-9]',word)!=None or re.search(r'(W|E|S|N)',rep)!=None \
                and re.search(r'^.*?[a-zA-Z]{2,}',rep)==None or re.search(r'°|\'|"',rep)!=None:
            return
def regular(coordinate):
    print type(coordinate)
    co = coordinate.encode('utf-8')
    print type(co)
    print co
    if re.search(r'[0-9]{1,2}°[0-9]{1,2}[’|\'][\s]{0,1}[N|S][\s|,|;]{0,2}[0-9]{1,3}°[0-9]{1,2}[’|\']{1,2}[\s]{0,1}[E|W]',co)!=None:
        print coordinate
        return True
    else:
        return False

if __name__=='__main__':
    #print coordinateRegularExtract('32° 10\'S<p>- 115° 56\'E<p>Thomsons 32° 09\'S<p>- 115° 50\'E'.split(' '))
    regular('29°40’N 53°30’E')


