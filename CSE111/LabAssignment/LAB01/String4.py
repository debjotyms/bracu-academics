givenStringA = input()
givenStringB = input()
temporaryString = ""
for character in givenStringA:
    if character in givenStringB:
        temporaryString = temporaryString+character
for character in givenStringB:
    if character in givenStringA:
        temporaryString = temporaryString+character
if len(temporaryString)==0:
    print('Nothing in common.')
else:
    print(temporaryString)