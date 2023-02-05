def mean(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum/len(a)

def stad(a):
    m=mean(a)
    sum=0
    for i in range(len(a)):
        sum+=(((a[i]-m)**2)/(len(a)-1))
    return sum**0.5

def awayStad(a):
    mn = mean(a)
    sd = stad(a)

    away = 1.5*sd
    c = 0

    for i in range(len(a)):
        if a[i] >= away+mn or a[i]<= away-mn:
            c+=1

    if c == 0:
        return None

    b = [0]*c
    idx = 0

    for i in range(len(a)):
        if a[i] >= away+mn or a[i]<= away-mn:
            b[idx] = a[i]
            idx+=1

    return b

a = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]

print(f"The mean of the numbers is: {round(mean(a), 12)}")
print(f"The standard deviation is: {round(stad(a), 2)}")
print(f"New array: {awayStad(a)}")