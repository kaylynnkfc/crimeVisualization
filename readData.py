import simplejson as json

#Creates and returns json object    
def createJsonObject(name):
    
    jsonFile = open(name)
    jsonContents = jsonFile.read()

    dataObject = json.loads(jsonContents)
        
    return dataObject


def getDataForYear(data, year, state):
    
    stateVal = 0
    
    for d in data: 
        if (d['Year'] == year):
            stateVal= d[state]
        
        
    print stateVal
    return stateVal     
    
    
def getAllDataForState(data, state):
    
    stateVals = {}
    
    for d in data: 
        stateVals[d['Year']] = d[state]
        
    return stateVals  