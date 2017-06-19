import geonameRelationDaoImpl

def addGeonameToWetlandRelation(geonames,wetlands):
    for wetland in wetlands:
        if wetland[2] == None:
            continue
        for geoname in geonames:
            if geoname == None:
                continue
            T = [geoname[1],geoname[2],geoname[3]]
            for geo in T:
                if geo == None:
                    continue
                if geo in wetland[2]:
                    geonameRelationDaoImpl.addRelation(geoname, wetland)
