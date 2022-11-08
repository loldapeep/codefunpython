import math
def isPrime(n):
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
count=0
for x in range(2, int(input())+1):
    if isPrime(x):
        count+=1
print(count)
