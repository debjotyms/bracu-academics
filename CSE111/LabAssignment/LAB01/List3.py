while True:
    givenString = input()
    if(givenString=='STOP'):
        break
    lst = [int(number) for number in givenString.split(' ')]
    lengthOfList = len(lst)-1
    maxNum = 0
    for element in range(len(lst)-1):
        difference = abs(lst[element]-lst[element+1])
        maxNum = max(difference,maxNum)
    if(maxNum<=lengthOfList):
        print('UB Jumper')
    else:
        print('Not UB Jumper')