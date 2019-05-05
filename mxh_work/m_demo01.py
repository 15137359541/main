import shelve
nameDict = {}

db = shelve.open('G:/main/broker.ph')
brokerDict=db['brokerDict']
print(brokerDict)

for brokerID, values in brokerDict.items():
    nameDict[values['name']] = brokerID
borkerList = []
print(nameDict)

db.close()
