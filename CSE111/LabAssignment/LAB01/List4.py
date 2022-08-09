listA = [int(number) for number in input().split(' ')]
listB = [int(number) for number in input().split(' ')]
for player in range(len(listB)):
    listB[player]+=listA[1]
valid = 0
for player in listB:
    if player<=5:
        valid+=1
print(valid//3)