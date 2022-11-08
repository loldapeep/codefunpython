import math
def isPrime(n):
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return x
    return "YES"
print(isPrime(int(input())))