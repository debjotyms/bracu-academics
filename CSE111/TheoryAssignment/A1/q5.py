def isPrime(i):
    for j in range(2,i):
        if i%j==0:
            return 0
    return 1

def primes(num):
    setOfPrimes = set({})
    for i in range(2,num+1):
        if(isPrime(i)):
            setOfPrimes.add(i)
    return setOfPrimes

studentID = str(22141001)
num = int(studentID[6:8])
print(primes(num))