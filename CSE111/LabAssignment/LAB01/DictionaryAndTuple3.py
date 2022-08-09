tempDictA = {'a':'1','b':'2','c':'1'}
tempDictB = {}
for value in tempDictA.values():
    tempDictB[value] = []
for key,value in tempDictA.items():
    tempDictB[value].append(key)
print(tempDictB)