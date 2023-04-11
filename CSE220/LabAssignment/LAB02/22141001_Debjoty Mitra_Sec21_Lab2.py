def printer(r2l, l2r):
    for i in range(2):
        for j in range(10):
            print(arr[i][j],end='')
        print()


def valid(arr):
    for i in range(2):
        scan = input()
        if len(scan) <= 10:
            for j in range(len(scan)):
                arr[i][j] = scan[j]
        else:
            print('Invalid Input Size!!!')
            return

    input("Your input is valid. Press any key and then press enter to continue!!!\n")
    
    r2lI = 0
    l2rI = 0
    r2lC = ''
    l2rC = ''

    for i in range(10):
        if 65<=ord(arr[0][i])<=90:
            r2lI = i
            r2lC = arr[0][i]
        if 65<=ord(arr[1][i])<=90:
            l2rI = i
            l2rC = arr[1][i]
    

    print(f"Top Board Start Character: {r2lC}")
    print(f"Top Board Start Index: {r2lI}")
    print(f"Bottom Board Start Character: {l2rC}")
    print(f"Bottom Board Start Index: {l2rI}")
    
    idxR2l = r2lI
    idxL2r = l2rI

    while(True):
        q = input("Press any key and then press enter to continue!!!")
        if q=='Q' or q == 'q':
            print(f"Top Board Start Character: {r2lC}")
            print(f"Top Board Start Index: {r2lI}")
            print(f"Bottom Board Start Character: {l2rC}")
            print(f"Bottom Board Start Index: {l2rI}")
            break
        
        ta = (idxR2l+10)%10
        tb = idxL2r%10

        for i in range(10):
            print(arr[0][ta],end='')
            ta-=1
            ta=(10+ta)%10
        
        idxR2l-=1
        print()

        for i in range(10):
            print(arr[1][tb],end='')
            tb+=1
            tb=tb%10

        idxL2r+=1
        print()

arr = [[' ']*10,[' ']*10]
valid(arr)