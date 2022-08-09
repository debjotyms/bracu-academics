givenString = input()
sNumber = 0
sWord = 0
for character in givenString:
    if 'a'<=character.lower()<='z':
        sWord+=1
    else:
        sNumber+=1
if sWord==len(givenString):
    print("WORD")
elif sNumber==len(givenString):
    print("NUMBER")
else:
    print("MIXED")