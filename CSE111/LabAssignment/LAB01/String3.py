givenString = input()
strt = 0
end = 0
flag = 0
for character in range(len(givenString)):
    if givenString[character].isupper() and flag==0:
        strt = character
        flag+=1
    elif givenString[character].isupper() and flag==1:
        end = character
        break
if end-1==strt:
    print("BLANK")
else:
    print(givenString[strt+1:end])