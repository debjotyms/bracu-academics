listNumer = int(input())
maxSum = float('-inf')
maxList = None
for testCase in range(listNumer):
    tempSum = 0
    tempList = [int(x) for x in input().split(' ')]
    for number in tempList:
        tempSum+=int(number)
    if(tempSum>maxSum):
        maxSum = tempSum
        maxList = tempList
print(maxSum)
print(maxList)