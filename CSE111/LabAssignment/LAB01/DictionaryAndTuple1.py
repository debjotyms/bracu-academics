dictionaryA = {'a': 100, 'b': 100, 'c': 200, 'd': 300}
dictionaryB = {'a': 300, 'b': 200, 'd': 400, 'e': 200}
dictionaryC = {}
for element in dictionaryA.keys():
    dictionaryC[element] = dictionaryA[element]
for element in dictionaryB.keys():
    try:
        dictionaryC[element] = dictionaryA[element] + dictionaryB[element]
    except:
        dictionaryC[element] = dictionaryB[element]
print(dictionaryC)
tpl = []
for element in dictionaryC.values():
    tpl.append(element)
tpl=set(tpl)
tpl=list(tpl)
tpl.sort()
tpl=tuple(tpl)
print(f'Values:{tpl}')