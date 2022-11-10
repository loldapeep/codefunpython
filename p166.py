import math
def isPrime(n):
    if n<=1: return 0
    else:
        for x in range (2,round(math.sqrt(n)+1)):
            if n%x==0:
                return 0
        return 1
print(isPrime(int(input())))