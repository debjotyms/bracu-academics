temporaryDictionary = {}
while True:
    number = input()
    if number=='STOP':
        break
    if number in temporaryDictionary:
        temporaryDictionary[number]+=1
    else:
        temporaryDictionary[number]=1
for element in temporaryDictionary:
    print(f'{element} - {temporaryDictionary[element]} times')