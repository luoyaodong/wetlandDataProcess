import convention
import positionDaoImpl

def positionAdd():
    results = convention.findDescription()
    for result in results:
        if result == None:
            continue
        positionDaoImpl.addPosition(result[0],result[1],result[3])
def geoFeatureAdd():
    results = convention.findDescription()
    for result in results:
        if result == None:
            continue
        positionDaoImpl.geoFeatureAdd(result[0],result[1],result[3],result[4],result[5])
