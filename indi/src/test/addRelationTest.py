import time
import convention
import coordinateDao
import geoname
import literature
import literatureDao
import metadata
import metadataDao
import plantRelationDao
import plants
import animals
import animalRelationDao
import positionDao
import geonameRelationDao


def plantsTest():
    now=time.strftime("%M:%S")
    plantRelationDao.findPlantRelation(plants.getPlantsSciName(), convention.findDescription())
    end=time.strftime("%M:%S")
    print (now+","+end)

def animalTest():
    now = time.strftime("%M:%S")
    animalRelationDao.findRelationToConention(animals.getAnimalSciName(),convention.findDescription())
    end = time.strftime("%M:%S")
    print (now+","+end)

def coordinateTest():
    now = time.strftime("%M:%S")
    coordinateDao.extractCoordinate()
    end = time.strftime("%M:%S")
    print (now+","+end)
def positionTest():
    now = time.strftime("%M:%S")
    positionDao.geoFeatureAdd()
    end = time.strftime("%M:%S")
    print (now+","+end)
def literatureDaoTest():
    now = time.strftime("%M:%S")
    literatureDao.findWetlandFromLiterature(literature.getLiterature(),convention.findDescription())
    literatureDao.deleteData()
    end = time.strftime("%M:%S")
    print (now+","+end)
def literatureToPlantTest():
    now = time.strftime("%M:%S")
    literatureDao.findPlantFromLiterature(literature.getLiterature(),plants.getPlantsSciName())
    end = time.strftime("%M:%S")
    print (now+","+end)
def literatureToAnimalTest():
    now = time.strftime("%M:%S")
    literatureDao.findAnimalFromLiterature(literature.getLiterature(),animals.getAnimalSciName())
    end = time.strftime("%M:%S")
    print (now+","+end)
def metadataToWetlandTest():
    now = time.strftime("%M:%S")
    metadataDao.findWetlandFromdatadata(metadata.getMetadata(),convention.findDescription())
    metadataDao.deleteData()
    end = time.strftime("%M:%S")
    print (now+","+end)
def metadataToPlantTest():
    now = time.strftime("%M:%S")
    metadataDao.findPlantFromdatadata(metadata.getMetadata(),plants.getPlantsSciName())
    end = time.strftime("%M:%S")
    print (now+","+end)

def metadataToAnimalTest():
    now = time.strftime("%M:%S")
    metadataDao.findAnimalFromdatadata(metadata.getMetadata(),animals.getAnimalSciName())
    end = time.strftime("%M:%S")
    print (now+","+end)


def plantSysnameToWetland():
    now = time.strftime("%H:%M:%S")
    plantRelationDao.findSynonymName(plants.getPlantsSynonym(),convention.findDescription())
    end = time.strftime("%H:%M:%S")
    print (now+","+end)

def plantSysnameToLiterature():
    now = time.strftime("%H:%M:%S")
    plantRelationDao.findSynonymNameToLiterature(plants.getPlantsSynonym(),literature.getLiterature())
    end = time.strftime("%H:%M:%S")
    print (now+","+end)
def plantSysnameToMetadata():
    now = time.strftime("%H:%M:%S")
    plantRelationDao.findSynonymNameToMetadata(plants.getPlantsSynonym(),metadata.getMetadata())
    end = time.strftime("%H:%M:%S")
    print (now+","+end)
def geoToWetland():
    now = time.strftime("%H:%M:%S")
    geonameRelationDao.addGeonameToWetlandRelation(geoname.getGeoname(),convention.findLocation())
    end = time.strftime("%H:%M:%S")
    print (now+","+end)
#positionTest()
#coordinateTest()
#animalTest()
#plantsTest()

# literatureDaoTest()
# literatureToPlantTest()
# literatureToAnimalTest()
#metadataToWetlandTest()
#metadataToPlantTest()
#metadataToAnimalTest()

#plantSysnameToWetland()
#plantSysnameToLiterature()
#plantSysnameToMetadata()

geoToWetland()
