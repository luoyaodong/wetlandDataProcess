def addAnimalToWetlandRelation(param, param1, param2, param3):
    pass


def findRelationToConention(animals,conventions):
    for con in conventions:
        if con[7] == None:
            continue
        for animal in animals:
            if animal[3] == None:
                continue
            if animal[3] in con[7]:
                addAnimalToWetlandRelation(animal[0],animal[1],animal[3],con[7])
import xlrd;
def readData():
    data = xlrd.open_workbook("window regulator.xlsx") #打开excel
    table = data.sheet_by_name("Sheet2")#读sheet
    nrows = table.nrows #获得行数
    result = []
    for i in range(1,nrows):  #
        rows  = table.row_values(i) #行的数据放在数组里
        sku = rows[0]
        keyword = str(rows[1]).split("-")[1] + " "+ str(rows[2]).replace("|"," ") + " window regulator"
        kind = rows[3]
        result.append([sku, keyword,kind])
    print(result)