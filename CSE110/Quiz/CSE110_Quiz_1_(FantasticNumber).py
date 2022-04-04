n = int(input("Please enter a number: "))
k=n
p_check=0
sum=0
if(n==1):
        p=0
for i in range(2,n+1):
    if(i==n):
        p_check=1
        break
    if(n%i==0):
        p_check=0
        break
if(p_check==0):
    print('Not Fantastic')
else:
    n=k
    while n!=0:
        r=n%10
        n=n//10
        sum=sum+r
    n=sum
    if(n==1):
        p=0
    for i in range(2,n+1):
        if(i==n):
            p_check=1
            break
        if(n%i==0):
            p_check=0
            break
    if(p_check==1):
        print('Fantastic')
    else:
        print('Not Fantastic')