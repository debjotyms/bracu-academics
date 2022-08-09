givenString = input()
sUpper = 0
sLower = 0
sDigit = 0
sSpecial = 0
for character in givenString:
    if character.isupper():
        sUpper+=1
    elif character.islower():
        sLower+=1
    elif character.isdigit():
        sDigit+=1
    elif character=='_' or character=='$' or character=='#' or character=='@':
        sSpecial+=1
flag = 0
if sUpper==0:
    if flag==1:
        print(', ',end='')
    print('Uppercase character missing',end='')
    flag = 1
if sLower==0:
    if flag==1:
        print(', ',end='')
    print('Lowercase character missing',end='')
    flag = 1
if sDigit==0:
    if flag==1:
        print(', ',end='')
    print('Digit missing',end='')
    flag = 1
if sSpecial==0:
    if flag==1:
        print(', ',end='')
    print('Special character missing',end='')
    flag = 1