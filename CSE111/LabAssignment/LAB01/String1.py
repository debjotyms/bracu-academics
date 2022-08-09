givenString = input()
sUpper = 0
sLower = 0
for character in givenString:
    if character.isupper():
        sUpper+=1
    else:
        sLower+=1
if(sUpper>sLower):
    print(givenString.upper())
else:
    print(givenString.lower())