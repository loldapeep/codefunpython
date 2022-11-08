import math
def isPrime(n):
    if n<=1: return False
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
def digit(n):
    if n==0:
        return 1
    else:
        i=0
        while 10**i<=n:
            i+=1
        return i
def ans(n):
    if isPrime(n):
        print("Good")
        print(digit(n))
    else: print("Bad")
ans(int(input()))