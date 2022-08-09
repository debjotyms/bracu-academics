list1 = []
list2 = []
while True:
    inp=input()
    if inp=="STOP":
        break
    else:
        inp=int(inp)
        list1.append(inp)
for element in list1:
    if element not in list2:
        list2.append(element)
for element in list2:
    count=0
    for element2 in list1:
        if element==element2:
            count+=1
    print(f'{element} - {count} times')