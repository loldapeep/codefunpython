import math
def isPrime(n):
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
for x in range (2,int(input())):
    if isPrime(x):
        print(x, end=" ")